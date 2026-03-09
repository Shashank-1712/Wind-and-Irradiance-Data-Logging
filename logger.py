import serial
import time
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0',9600)

file = open("weather_data3.csv","a")

while True:

    line = ser.readline().decode().strip()
    wind,irr = line.split(",")

    timestamp = datetime.now()

    log = f"{timestamp},{wind},{irr}"
    
    print(log)

    file.write(log + "\n")
    file.flush()
