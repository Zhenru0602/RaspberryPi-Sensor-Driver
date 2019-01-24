# _____ _____ _____ __ __ _____ _____ 
#|     |   __|     |  |  |     |     |
#|  |  |__   |  |  |_   _|  |  |  |  |
#|_____|_____|_____| |_| |_____|_____|
#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor
#  
import time
import dht11
import RPi.GPIO as GPIO

Temp_sensor = 17  #temp orange


class TempSensor:
  def __init__(self):   
    GPIO.setwarnings(False)
    GPIO.cleanup()	
    GPIO.setmode(GPIO.BCM)
    self.instance = dht11.DHT11(pin = Temp_sensor)
    
  def read(self):
    result = self.instance.read()
    if result.temperature != 0 | result.humidity != 0:
      return {'temp':result.temperature, 'humi':result.humidity}
    else:
      return None
