from pijuice import PiJuice # Import pijuice module
import time

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object

f = open(f"/home/kazuya/LoRaPos/raspi/data/pijuice.csv", "a")
f.writelines(f"time, charge_level\n")

while True:
    f = open(f"/home/kazuya/LoRaPos/raspi/data/pijuice.csv", "a")

    measured_time = time.time_ns()
    level = pijuice.status.GetChargeLevel()["data"]

    try:
        f.writelines(f"{measured_time}, {level} \n")
    except:
        pass
    time.sleep(10)
    f.close()
