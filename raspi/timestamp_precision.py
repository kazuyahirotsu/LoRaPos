# Python program to explain time.clock_getres() method

# importing time module
import time


# clk_id for System-wide real-time clock
clk_id1 = time.CLOCK_REALTIME

# clk_id for monotonic clock
clk_id2 = time.CLOCK_MONOTONIC

# clk_id for monotonic (Raw hardware
# based time) clock
clk_id3 = time.CLOCK_MONOTONIC

# clk_id for Thread-specific CPU-time clock
clk_id4 = time.CLOCK_THREAD_CPUTIME_ID

# clk_id for High-resolution
# per-process timer from the CPU
clk_id5 = time.CLOCK_PROCESS_CPUTIME_ID


# Get the precision (Resolution)
# of the above specified clock clk_ids
# using time.clock_getres() method
precision1 = time.clock_getres(clk_id1)
precision2 = time.clock_getres(clk_id2)
precision3 = time.clock_getres(clk_id3)
precision4 = time.clock_getres(clk_id4)
precision5 = time.clock_getres(clk_id5)

# Print the precision (resolution)
print("Precision of system-wide real-time clock:", precision1)
print("Precision of monotonic clock:", precision2)
print("Precision of monotonic (raw-hardware based time) clock:",
												precision3)
print("Precision of thread-specific CPU time clock:", precision4)
print("Precision of per-process time from the CPU:", precision5)
