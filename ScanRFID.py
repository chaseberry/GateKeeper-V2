import Adafruit_BBIO.UART as uart
import serial

uart.setup("UART5")


ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600, timeout=15)


print("\n")
card = ser.read(12)
print(card[1:])
if(card[1:] == "06008E52BF6"):
	print("access granted")
	import open.py

else:
	print("Denied")

