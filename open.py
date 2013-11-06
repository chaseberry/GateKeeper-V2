import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_42",GPIO.OUT)
GPIO.setup("P9_41",GPIO.OUT)

GPIO.output("P9_42",GPIO.HIGH)

time.sleep(.2)

GPIO.output("P9_42",GPIO.LOW)

time.sleep(5)

GPIO.output("P9_41",GPIO.HIGH)
time.sleep(.2)
GPIO.cleanup()
