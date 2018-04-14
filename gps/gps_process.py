#!/env/python3

import serial
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("/dev/") if isfile(join("/dev/", f))]

if __name__ == "__main__":
	for i in listdir("/dev"):
		try:
			ser = serial.Serial(port="/dev/"+str(i), baudrate=9600,parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS)
			print(i)
			reportID = ser.read()
			dataPack = ser.read()
			command  = ser.read()
			address0 = ser.read()
			address1 = ser.read()
			print(reportID, dataPack, command, address0, address1)
		except:
			"""error..."""
