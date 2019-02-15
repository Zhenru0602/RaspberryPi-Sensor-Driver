#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor
#  
import time
import dht11
import RPi.GPIO as GPIO

# rasp pin setup
Temp_sensor = 17  #temp orange

# return value are two ints (temp, humid)
class TempSensor:
  def __init__(self):   
    GPIO.setmode(GPIO.BCM)
    self.instance = dht11.DHT11(pin = Temp_sensor)
    
  def read(self):
    result = self.instance.read()
    if result.temperature != 0 or result.humidity != 0:
      return {'temp':result.temperature, 'humi':result.humidity}
    else:
      return None
