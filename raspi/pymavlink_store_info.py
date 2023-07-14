from pymavlink import mavutil
import time
import sys

import logging

# logging.basicConfig(format='%(asctime)s %(message)s',filename='solarpanel_voltage.log', encoding='utf-8', level=logging.DEBUG)

root_logger= logging.getLogger()
root_logger.setLevel(logging.DEBUG) # or whatever
handler = logging.FileHandler('/home/kazuya/LoRaPos/raspi/data/test.log',  encoding='utf-8') # or whatever
handler.setFormatter(logging.Formatter('%(asctime)s %(message)s')) # or whatever
root_logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

def request_message_interval(message_id: int, frequency_hz: float):
    """
    Request MAVLink message in a desired frequency,
    documentation for SET_MESSAGE_INTERVAL:
        https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL

    Args:
        message_id (int): MAVLink message ID
        frequency_hz (float): Desired frequency in Hz
    """
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
        message_id, # The MAVLink message ID
        1e6 / frequency_hz, # The interval between two messages in microseconds. Set to -1 to disable and 0 to request default rate.
        0, 0, 0, 0, # Unused parameters
        0, # Target address of message stream (if message has target address fields). 0: Flight-stack default (recommended), 1: address of requestor, 2: broadcast.
    )

def send_heartbeat(master):
    if master.mavlink10():
        master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID,
                                  0, 0, 0)
    else:
        MAV_GROUND = 5
        MAV_AUTOPILOT_NONE = 4
        master.mav.heartbeat_send(MAV_GROUND, MAV_AUTOPILOT_NONE)

# Start a connection listening on a USB port
master = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)
print("connection initializing")

# Wait for the first heartbeat 
# This sets the system and component ID of remote system for the link
send_heartbeat(master)
print("heartbeat sent to master")
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))


# # Configure AHRS2 message to be sent at 1Hz
# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_AHRS2, 1)

# # Configure ATTITUDE message to be sent at 2Hz
# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_ATTITUDE, 2)

# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_GPS_RAW_INT, 5)
start_time = time.time_ns()
f = open(f"/home/kazuya/LoRaPos/raspi/data/pixhawk_gps_{start_time}.csv", "a")
f.writelines(f"received_time, altitude, lat, lon, alt\n")
# Get some information !
while True:
    f = open(f"/home/kazuya/LoRaPos/raspi/data/pixhawk_gps_{start_time}.csv", "a")
    try:
        # print(master.recv_match(type='ALTITUDE').to_dict()['altitude_local'])
        msg = master.recv_match()
        if msg.get_type() == 'ALTITUDE':
            # print("altitude_local: ", msg.to_dict()['altitude_local'])
            logging.info("altitude_local: " + str(msg.to_dict()['altitude_local']))
            f.writelines(f"{time.time_ns()}, {msg.to_dict()['altitude_local']}, , , \n")
        elif msg.get_type() == 'GPS_RAW_INT':
            logging.info("lat: " + str(msg.to_dict()['lat']))
            logging.info("lon: " + str(msg.to_dict()['lon']))
            logging.info("alt: " + str(msg.to_dict()['alt']))
            f.writelines(f"{time.time_ns()}, , {msg.to_dict()['lat']}, {msg.to_dict()['lon']}, {msg.to_dict()['alt']}\n")
            # print("lat: ", msg.to_dict()['lat'])
            # print("lon: ", msg.to_dict()['lon'])
            # print("alt: ", msg.to_dict()['alt'])
    except:
        pass
    finally:
        f.close()
    f.close()
    time.sleep(0.01)
