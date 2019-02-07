import socket
import time
import RPi.GPIO as GPIO

import sys
sys.path.append("../sensors/")

import tempSensor
import smokeSensor
import motionSensor
import waterLevelSensor

#This socket (TCP/IP) is to open a port to listen the connection socket request from Android/Other OS.
#Before using, the PORT should be mannually set

#socket info
connected = False
HOST = ''                 
PORT = 6666

#sensor data init
temperature = None
humidity = None
smoke = None
motion = None

GPIO.setwarnings(False)
GPIO.cleanup()
tempSensor = tempSensor.TempSensor()
smokeSensor = smokeSensor.SmokeSensor()
motionSensor = motionSensor.MotionSensor()
waterLevelSensor = waterLevelSensor.WaterLevelSensor()

while 1:
    try:
        if connected == False:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            print('Connected by', addr)
            connected = True
        
	#e.g. sensors can be choosen for different applications
        #e.g. read temperature and humidity    
        tempResult = tempSensor.read()
        if tempResult != None:
            temperature = tempResult['temp']
            humidity = tempResult['humi']

        #e.g. read smoke
        smoke = smokeSensor.read()

        #e.g. read motion
        motion = motionSensor.read()

        #e.g. read water level
        water_level = waterLevelSensor.read()

        #function to create json string contains all data, can be customized
        jsonString = '{"temperature":'+str(temperature)+', "humidity":'+str(humidity)+',"smoke":'+str(smoke)+', "motion":'+str(motion)+', "water_level":'+str(water_level)+'}'
        conn.send(jsonString)
        time.sleep(2)
    except socket.error:
        conn.close()
        s.close()
        connected = False
        print("restart connection!")

