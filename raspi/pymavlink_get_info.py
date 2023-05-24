from pymavlink import mavutil
import time
import sys

# Start a connection listening on a UDP port
master = mavutil.mavlink_connection('/dev/ttyACM0')
print("connection initializing")
# Wait for the first heartbeat 
# This sets the system and component ID of remote system for the link
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))


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

# # Configure AHRS2 message to be sent at 1Hz
# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_AHRS2, 1)

# # Configure ATTITUDE message to be sent at 2Hz
# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_ATTITUDE, 2)

# request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_GPS_RAW_INT, 5)


# Get some information !
while True:
    try:
        # print(master.recv_match(type='ALTITUDE').to_dict()['altitude_local'])
        msg = master.recv_match()
        if msg.get_type() == 'ALTITUDE':
            print("altitude_local: ", msg.to_dict()['altitude_local'])
        elif msg.get_type() == 'GPS_RAW_INT':
            print("lat: ", msg.to_dict()['lat'])
            print("lon: ", msg.to_dict()['lon'])
            print("alt: ", msg.to_dict()['alt'])
    except:
        pass
    time.sleep(0.01)