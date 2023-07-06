import time
from tqdm import tqdm
from pylab import *
from rtlsdr import *

sdr = RtlSdr()

# configure device
sdr.sample_rate = 1.0e6
sdr.center_freq = 915e6
sdr.gain = 4

results_list = [[],[]]

while(True):
    try:
        for i in tqdm(range(1000)):
            samples = sdr.read_samples()
            # use matplotlib to estimate and plot the PSD
            results = psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
            results_list[0].append(time.time_ns())
            results_list[1].append(10*np.log10(np.mean(results[0][384:641])))

        f = open(f"rssi_{time.time_ns()}.csv", "a")
        for i in range(len(results_list[0])):
            f.writelines(str(results_list[0][i])+", "+str(results_list[1][i])+"\n")
        f.close()
    except:
        sdr.close()