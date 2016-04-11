from threading import Thread
import serial

import time

import MainApp


def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def tryConnect():
	newSer=0
	for i in range(0,9):
		try:
			newSer=serial.Serial('/dev/ttyUSB'+str(i),9600)
			print ('/dev/ttyUSB'+str(i))
			newSer.flushInput()
			newSer.flushOutput()
			time.sleep(0.1)
			return newSer
		except (serial.serialutil.SerialException):
			pass
	for i in range(0,9):
		try:
			newSer=serial.Serial('/dev/ttyACM'+str(i),9600)
			print ('/dev/ttyACM'+str(i))
			newSer.flushInput()
			newSer.flushOutput()
			time.sleep(0.1)
			return newSer
		except (serial.serialutil.SerialException):
			pass
	print ("Arduino not connected")
	time.sleep (1)
	return 0

class ArduinoReader(Thread):
	def __init__(self,MainUnit):
		Thread.__init__(self)
		self.MainUnit=MainUnit
	def run(self):

		ser=tryConnect()
		while(True):
			try:
				if (ser==0):
					ser=tryConnect()
				else:
					if self.MainUnit.getChanged():
						ser.write("title "+str(self.MainUnit.getTitle())+'\0')
						ser.write("artist "+str(self.MainUnit.getArtist())+'\0')
						self.MainUnit.setChanged(False)
					if (ser.inWaiting()>0):
						input=ser.readline()
						print(input)
						if (input=="start\r\n"):
							try:
								ser.write("title "+str(self.MainUnit.getTitle())+'\0')
								ser.write("artist "+str(self.MainUnit.getArtist())+'\0')
							except (Exception,e):
								print (str(e))
						if RepresentsInt(input):
							lightvalue=min(max(0,int(input)),100)
							self.MainUnit.setLight(lightvalue)
						if (input=="a\r\n"):
							self.MainUnit.previous()
							self.MainUnit.previousSong()
						elif (input=="b\r\n"):
							self.MainUnit.play()
						elif (input=="c\r\n"):
							self.MainUnit.nextsong()
						elif (input=="d\r\n"):
							self.MainUnit.louder()
						elif (input=="e\r\n"):
							self.MainUnit.lower()
						elif (input=="g\r\n"):
							self.MainUnit.entered()
						elif (input=="f\r\n"):
							self.MainUnit.left();
			except (Exception):
				print (str(Exception))
				ser=tryConnect()
			time.sleep(0.2)