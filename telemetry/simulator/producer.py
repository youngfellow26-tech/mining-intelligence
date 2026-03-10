
import random, time

machines = ["Truck-101","Drill-22","Excavator-9"]

while True:
    m = random.choice(machines)
    payload = {
        "machine": m,
        "temperature": random.randint(60,120),
        "vibration": random.random(),
        "fuel_level": random.randint(10,100)
    }
    print("Telemetry:", payload)
    time.sleep(2)
