import time
from rtlsdr import *
import matplotlib.pyplot as plt
import numpy as np

sdr = RtlSdr()

# configure device
sdr.sample_rate = 1.0e6
sdr.center_freq = 915e6
sdr.gain = 4

results_list = [[],[]]
start_time = time.time_ns()

f = open(f"/home/kazuya/LoRaPos/raspi/data/rtlsdr_rssi_{start_time}.csv", "a")
f.writelines(f"received_time, rssi\n")
while(True):
    try:
        f = open(f"/home/kazuya/LoRaPos/raspi/data/rtlsdr_rssi_{start_time}.csv", "a")
        for i in range(1000):
            samples = sdr.read_samples()
            # use matplotlib to estimate and plot the PSD
            results = plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
            # results_list[0].append(time.time_ns())
            # results_list[1].append(10*np.log10(np.mean(results[0][384:641])))
            # f.writelines(str(time.time_ns())+", "+str(10*np.log10(np.mean(results[0][384:641])))+"\n")
            time.sleep(0.01)
        f.close()
        time.sleep(0.01)
    except Exception as e:
        print(e)
        f.close()
        sdr.close()
        sdr = RtlSdr()

    finally:
        f.close()
        sdr.close()