import serial
import json
import time

PORT = 'COM3' 
BAUD_RATE = 9600 # communication speed between the Arduino and the  Python script via the serial port

arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
time.sleep(2)  # Arduino resetpython serial_reader.py

print("Reading serial data from Arduino...")

while True:
    try:
        line = arduino.readline().decode('utf-8').strip()
        print("Received:", line)  

        data = json.loads(line)

        if "solar" in data and "humidity" in data:
            with open("sensor_data.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            print("Unexpected data format")

    except json.JSONDecodeError:
        print("Malformed JSON, skipping line.")
    except Exception as e:
        print("Error:", e)
        break
