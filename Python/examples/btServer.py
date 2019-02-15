import bluetooth
import socket
import time
import json
import RPi.GPIO as GPIO

import sys
sys.path.append("../sensors/")

import tempSensor
import smokeSensor
import motionSensor
import waterLevelSensor

# This program is a bluetooth receiver to receive the data
connected = False
PORT = 3
L = 1 #number of listening

#sensor data init
temp = None
humd = None
Sm = None
Mo = None
Wt = None

GPIO.setwarnings(False)
GPIO.cleanup()
tempSensor = tempSensor.TempSensor()
smokeSensor = smokeSensor.SmokeSensor()
motionSensor = motionSensor.MotionSensor()
waterLevelSensor = waterLevelSensor.WaterLevelSensor()


while 1:
        try:
                if not connected:
                        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                        s.bind(('', PORT))
                        s.listen(L)
                        client, clientInfo = s.accept()
                        print('Connected by', clientInfo)
                        connected = True

                # read temperature and humidity data
                T = tempSensor.read()
                if T != None:
                        temp = T['temp']
                        humd = T['humi']
                # read smoke data
                Sm = smokeSensor.read()
                # read motion data
                Mo = motionSensor.read()
                # read water level data
                Wt = waterLevelSensor.read()

                data = {"temperature":temp,"humidity":humd,"smoke":Sm,"motion":Mo,"water_level":Wt}
                jsonString = json.dumps(data)
                client.send(jsonString)
                time.sleep(2)

        except socket.error:
                client.close()
                s.close()
                connected = not connected
                print("restarting connection")
                continue

        except KeyboardInterrupt:
                client.close()
                s.close()
                break
                
#data = client.recv(1024)
#if data:
#print(data)

