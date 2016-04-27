from threading import Thread

import time

import subprocess

from MainApp import *

class WhistlingDetector(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		subprocess.Popen(["whistle_control/./whistle_control"])

class FileStreamReader(Thread):
	"""
	lasthit=0
	firsthit=0
	def hit(self):
		print("hit")
		if (self.firsthit==0):
			self.firsthit=time.time()
		self.lasthit=time.time()
		print(1.0*self.lasthit)
		print(1.0*self.firsthit)
	def miss(self):
		if (((time.time()-self.lasthit)>1) and (self.lasthit!=0)):

			duration=self.lasthit-self.firsthit
			print("duration "+str(duration))
			self.lasthit=0
			self.firsthit=0
			if (duration<0.3):
				pass
			elif(duration<1):
				self.MainUnit.play()
			elif(duration<2.5):
				self.MainUnit.nextsong()
			elif(duration<5):
				self.MainUnit.previousSong()
	"""
	lasthit=0
	firsthit=0
	def hit(self):
		print("hit")
		if (self.firsthit==0):
			self.firsthit=time.time()
		self.lasthit=time.time()
		print(1.0*self.lasthit)
		print(1.0*self.firsthit)

	def miss(self):
		if (((time.time()-self.lasthit)>1) and (self.lasthit!=0)):

			duration=self.lasthit-self.firsthit
			print("duration "+str(duration))
			self.lasthit=0
			self.firsthit=0
			if (duration<2):
				print ("to short")
				pass
			elif (duration<4):
				self.MainUnit.stop()
			else:
				self.MainUnit.nextsong()



	def __init__(self,MainUnit):
		Thread.__init__(self)
		self.MainUnit=MainUnit

	def run(self):
		import io
		#subprocess.Popen(["./whistle_control/whistle_control&"])
		#os.system("./whistle_control/whistle_control ")
		f = io.open("outputfile.txt")
		next=""
		while True:
			next=f.readline()
			if (next==""):
				break
		while True:

			if (self.MainUnit.WhistleOn):
				next=f.readline().strip()
				if (next!=""):
					self.hit()
					time.sleep(0.01)
				else:
					self.miss()
					time.sleep(0.01)
			else:
				sleep(1)
				while True:
					next=f.readline()
					if (next==""):
						break

