import board
import busio
import digitalio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D25)

import adafruit_rfm9x
import time
import random

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth, rfm9x.bw_bins)
rfm9x.ack_retries = 0
rfm9x.spreading_factor = 7
rfm9x.signal_bandwidth = 250000
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth)
data_to_send = bytes("hello\r\n","utf-8")

while True:
    rfm9x.send(data_to_send)
    print(f"Data sent: {data_to_send}")
    wait_time = random.uniform(0, 1)
    print("wait for ", wait_time)
    time.sleep(wait_time)
