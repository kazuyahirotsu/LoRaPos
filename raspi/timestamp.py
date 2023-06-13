import math
import time
import numpy as np

LOOPS = 10 ** 6

delta_list = [abs(time.time_ns() - time.time_ns())
          for _ in range(LOOPS)]
min_dt = min(filter(bool, delta_list))
print("min time_ns() delta: %s ns" % min_dt)
print("std: ", np.std(delta_list))
print("min: ", np.min(delta_list))
print("mean: ", np.mean(delta_list))
print("max: ", np.max(delta_list))

delta_list = [abs(time.time() - time.time())
          for _ in range(LOOPS)]
min_dt = min(filter(bool, delta_list))
print("min time() delta: %s ns" % math.ceil(min_dt * 1e9))
print("std: ", np.std(delta_list))
print("min: ", np.min(delta_list))
print("mean: ", np.mean(delta_list))
print("max: ", np.max(delta_list))

delta_list = [abs(time.process_time_ns() - time.process_time_ns())
          for _ in range(LOOPS)]
min_dt = min(filter(bool, delta_list))
print("min process_time_ns() delta: %s ns" % min_dt)
print("std: ", np.std(delta_list))
print("min: ", np.min(delta_list))
print("mean: ", np.mean(delta_list))
print("max: ", np.max(delta_list))

delta_list = [abs(time.perf_counter_ns() - time.perf_counter_ns())
          for _ in range(LOOPS)]
min_dt = min(filter(bool, delta_list))
print("min perf_counter_ns() delta: %s ns" % min_dt)
print("std: ", np.std(delta_list))
print("min: ", np.min(delta_list))
print("mean: ", np.mean(delta_list))
print("max: ", np.max(delta_list))

delta_list = [abs(time.monotonic_ns() - time.monotonic_ns())
          for _ in range(LOOPS)]
min_dt = min(filter(bool, delta_list))
print("min monotonic_ns() delta: %s ns" % min_dt)
print("std: ", np.std(delta_list))
print("min: ", np.min(delta_list))
print("mean: ", np.mean(delta_list))
print("max: ", np.max(delta_list))
