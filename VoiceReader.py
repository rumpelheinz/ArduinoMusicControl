from threading import Thread
from time import sleep

import speech_recognition as sr



def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

class Recognizerthread(Thread):
	def __init__(self,MainApp,audio,r):
		Thread.__init__(self)
		self.r=r
		self.audio=audio
		self.MainApp=MainApp
	def run(self):

		try:
			result=self.r.recognize_google(self.audio)
			##result=r.recognize_google(audio)
			list=result.split(" ")
			lastword=""
			secondlastword=""
			command=""
			sound=-1;
			for i in list:
				print (i)
				if (i=="play" or i=="playing"):
					command="play"
				if (i=="next"):
					command="next"
				if (i=="previous" or i=="last" or (i=="back" and lastword=="go") ):
					command="previous"
				if (i=="up" ):
					if (lastword=="volume"):
						command="louder"
				if (i=="down" ):
					if (lastword=="volume"):
						command="louder"
				if (i=="stop" ):
					command="stop"
				if RepresentsInt(i):
					if (lastword=="volume" or secondlastword=="volume"):
						sound=min(max(0,int(i)),100)
				secondlastword=lastword
				lastword=i


			print("Google thinks you said : " + result)
			if (command=="next"):
				print("you said next")
				self.MainApp.nextsong()
			elif (sound!=-1):
				self.MainApp.setVolume(sound)
			elif (command=="louder"):
				print("you said louder")
				self.MainApp.louder()
			elif (command=="quiter"):
				print("you said quiter")
				self.MainApp.lower()
			elif (command=="previous"):
				print("you said previous")
				self.MainApp.previousSong()
			elif (command=="play"):
				print("you said play")
				self.MainApp.play()
			elif (command=="stop"):
				print("you said stop")
				self.MainApp.stop()
		except sr.UnknownValueError:
			print("Google could not understand audio")
		except sr.RequestError as e:
			print("Google error; {0}".format(e))

class VoiceReader(Thread):
	def __init__(self,MainApp):
		Thread.__init__(self)
		self.MainApp=MainApp
	def run(self):

		r = sr.Recognizer()
		while (True):
			if (self.MainApp.VoiceOn):
				with sr.Microphone() as source:
					print("Say something!")

					while True:
						try:
							audio = r.listen(source,5)
							break
						except sr.WaitTimeoutError:
							print ("Retrying")

					print("Recognising sound")
					Recognizerthread(self.MainApp,audio,r).start()
			else:
				print ("Voice: "+str(self.MainApp.VoiceOn)+" , Arduino: "+ str(self.MainApp.ArduinoEnabled)+" , Whistle: "+str(self.MainApp.WhistleOn))
				sleep(1)
