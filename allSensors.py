import time
import tempSensor
import smokeSensor
import motionSensor

temperature = None
humidity = None
smoke = None
motion = None

tempSensor = tempSensor.TempSensor()
smokeSensor = smokeSensor.SmokeSensor()
motionSensor = motionSensor.MotionSensor()

while 1:
    tempResult = tempSensor.read()
    if tempResult != None:
        temperature = tempResult['temp']
        humidity = tempResult['humi']

    smoke = smokeSensor.read()

    motion = motionSensor.read()
    
    print("temp: " + str(temperature))
    print("humi: " + str(humidity))
    print("smoke: " + str(smoke))
    print("motion: " + str(motion))
    
    time.sleep(2)
