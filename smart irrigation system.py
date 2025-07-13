import time
import random

# Function to simulate soil moisture sensor value (0 to 100)
def read_soil_moisture():
    return random.randint(20, 100)

# Threshold value below which the pump should turn ON
MOISTURE_THRESHOLD = 50

# Main loop
while True:
    moisture = read_soil_moisture()
    print(f"Soil moisture level: {moisture}%")

    if moisture < MOISTURE_THRESHOLD:
        print("Status: Soil is dry. Turning pump ON 💧")
    else:
        print("Status: Soil moisture is sufficient. Pump OFF ✅")

    print("-" * 40)
    time.sleep(5)  # wait 5 seconds before next reading