import RPi.GPIO as GPIO
import time

SPICLK = 11  #mq2 orange
SPIMISO = 9 #mq2 brown
SPIMOSI = 10 #mq2 purple
SPICS = 8 #mq2 blue
ADC_NUM = 0

class WaterLevelSensor:
    def __init__(self):

            GPIO.setmode(GPIO.BCM)		#to specify whilch pin numbering system
            # set up the SPI interface pins
            GPIO.setup(SPIMOSI, GPIO.OUT)
            GPIO.setup(SPIMISO, GPIO.IN)
            GPIO.setup(SPICLK, GPIO.OUT)
            GPIO.setup(SPICS, GPIO.OUT)
            
             
    #read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
    def read(self):
            if ((ADC_NUM > 7) or (ADC_NUM < 0)):
                    return -1
            GPIO.output(SPICS, True)	

            GPIO.output(SPICLK, False)  # start clock low
            GPIO.output(SPICS, False)     # bring CS low

            commandout = ADC_NUM
            commandout |= 0x18  # start bit + single-ended bit
            commandout <<= 3    # we only need to send 5 bits here
            for i in range(5):
                    if (commandout & 0x80):
                            GPIO.output(SPIMOSI, True)
                    else:
                            GPIO.output(SPIMOSI, False)
                    commandout <<= 1
                    GPIO.output(SPICLK, True)
                    GPIO.output(SPICLK, False)

            adcout = 0
            # read in one empty bit, one null bit and 10 ADC bits
            for i in range(12):
                    GPIO.output(SPICLK, True)
                    GPIO.output(SPICLK, False)
                    adcout <<= 1
                    if (GPIO.input(SPIMISO)):
                            adcout |= 0x1

            GPIO.output(SPICS, True)
            
            adcout >>= 1       # first bit is 'null' so drop it
            value = "%.1f"%(adcout/400.0*100.0)+"%"
            return value
	
    


