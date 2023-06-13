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
rfm9x.spreading_factor =7 
rfm9x.signal_bandwidth = 250000
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth)
# data_to_send = bytes(" ","utf-8")
data_to_send = bytes(1)
rfm9x.enable_crc = False
print(rfm9x.coding_rate, rfm9x.enable_crc, rfm9x.preamble_length, rfm9x.ack_wait)
while True:
    start_time = time.process_time_ns()
    rfm9x.send(data_to_send)
    finish_time = time.process_time_ns()
    print("transmission time: ", finish_time - start_time)
    time.sleep(1)
