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
print(rfm9x.ack_retries, rfm9x.spreading_factor, rfm9x.signal_bandwidth)
data_to_send = bytes("hello\r\n","utf-8")

def send_data_with_aloha(data):
    sent = False
    while sent:
        rfm9x.send(data)
        print(f"Data sent: {data}")
        
        # Check for an acknowledgment from the receiver
        packet = rfm9x.receive(timeout=2.0)  # adjust timeout as necessary
        if packet is not None:
            packet_text = str(packet, 'ascii')
            if packet_text == "ACK":
                print("Acknowledgment received.")
                sent = True
                return
            else:
                print("Unexpected packet received: {packet_text}. Retransmitting data...")
        else:
            print("No acknowledgment received. Retransmitting data...")
        
        # Wait for a random period before retransmitting to reduce the chance of collisions
        time.sleep(random.uniform(0, 1))

while True:
    send_data_with_aloha(data_to_send)
    print(data_to_send)
    time.sleep(0.5)