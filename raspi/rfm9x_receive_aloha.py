import board
import busio
import digitalio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D25)

import adafruit_rfm9x
import time

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth, rfm9x.bw_bins)
rfm9x.ack_retries = 0
rfm9x.spreading_factor = 7 
rfm9x.signal_bandwidth = 250000
rfm9x.enable_crc = False
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth)

packets = []
start_time = time.time_ns()
f = open(f"/home/kazuya/LoRaPos/raspi/data/lora_module_received_{start_time}.csv", "a")
f.writelines(f"received_time, packet_text, rssi\n")

while True:
    f = open(f"/home/kazuya/LoRaPos/raspi/data/lora_module_received_{start_time}.csv", "a")
    packet = rfm9x.receive()
    received_time = time.time_ns()
    print("time: ", received_time)
    if packet is None:
        # Packet has not been received
        print("Received nothing! Listening again...")
    else:
        try:
            
            # Received a packet!
            print("Received (raw bytes): {0}".format(packet))

            packet_text = str(packet, "ascii")
            print("Received (ASCII): {0}".format(packet_text))
            rssi = rfm9x.last_rssi
            print("Received signal strength: {0} dB".format(rssi))

            packets.append([received_time, packet_text, rssi])
            f.writelines(f"{received_time}, {packet_text}, {rssi}\n")
        except:
            pass

    f.close()
