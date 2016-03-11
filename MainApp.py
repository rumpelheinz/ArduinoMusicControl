import os
from time import sleep

class MainUnit:
	print(__name__)

	ArduinoEnabled=True
	WhistleControlEnabled=True
	WebGuiEnabled=True
	SpotifyEnabled=True
	ListenerEnabled=True
	AlsaSoundEnabled=True
	VoiceRecognitionEnabled=True
	EspeakEnabled=True



	def __init__(self):
		self.VoiceOn=True
		self.WhistleOn=True
		self.restart=False
		self.artist="  Na"
		self.title="  Na"
		self.changed=False

		if self.WhistleControlEnabled:
			import WhistlingCommands

		if self.VoiceRecognitionEnabled:
			import VoiceReader

		if self.ArduinoEnabled:
			import Arduino

		if self.SpotifyEnabled:
			import MusicChangedListener

		if (self.SpotifyEnabled or self.AlsaSoundEnabled):
			import MusicPlayer

		if self.WebGuiEnabled:
			from WebGui import WebGui
			self.Gui=WebGui()

		self.MusicPlayer=MusicPlayer.MusicPlayer()

		if self.WhistleControlEnabled:
			whistleDetector=WhistlingCommands.WhistlingDetector()
			whistleDetector.start()
			sleep(0.1)
			fileStreamReaderThread=WhistlingCommands.FileStreamReader(self)
			fileStreamReaderThread.start()

		if self.ListenerEnabled:
			listenerThread=MusicChangedListener.Listener(self)
			listenerThread.start()

		if self.VoiceRecognitionEnabled:
			voiceThread=VoiceReader.VoiceReader(self)
			voiceThread.start()

		if self.ArduinoEnabled:
			arduinoReader=Arduino.ArduinoReader(self)
			arduinoReader.start()

		if self.WebGuiEnabled:
			print "starting gui"
			self.Gui.run(self)
			print("after")

	def getChanged(self):
		return self.changed

	def setChanged(self,newchanged):

		self.changed=newchanged

	def toggleWhistle(self):
		if self.WhistleOn:
			self.WhistleOn=False
		else:
			self.WhistleOn=True

	def toggleVoice(self):
		if self.VoiceOn:
			self.VoiceOn=False
		else:
			self.VoiceOn=True


	def setArtist(self,newartist):
		self.artist=newartist
		print(self.artist)


	def setTitle(self,newtitle):
		self.title=newtitle

	def getTitle(self):
		return self.title

	def getArtist(self):


		return self.artist

	def getVolume(self):
		if self.AlsaSoundEnabled:
			return self.MusicPlayer.getVolume()

	def louder(self):
		print("Louder")
		if self.EspeakEnabled:
			os.system("espeak Louder&")
		if self.AlsaSoundEnabled:
			self.MusicPlayer.louder()
		if self.WebGuiEnabled:
			self.Gui.emitVolume(self.MusicPlayer.getVolume())

	def lower(self):
		print("Lower")
		if self.EspeakEnabled:
			os.system("espeak Lower&")
		if self.AlsaSoundEnabled:
			self.MusicPlayer.lower()
		if self.WebGuiEnabled:
			self.Gui.emitVolume(self.MusicPlayer.getVolume())

	def setVolume(self,sound):
		print("Setting Sound to "+str(sound)+"'")
		if self.EspeakEnabled:
			os.system("espeak 'Setting Sound to "+str(sound)+"'&")
		if self.AlsaSoundEnabled:
			self.MusicPlayer.setVolume(sound)
		if self.WebGuiEnabled:
			self.Gui.emitVolume(sound)

	def previous(self):
		print("Previous")
		if self.EspeakEnabled:
			os.system("espeak Previous&")
		if self.SpotifyEnabled:
			self.MusicPlayer.previous()

	def stop(self):
		if self.EspeakEnabled:
			os.system("espeak Stop&")
		if self.SpotifyEnabled:
			self.MusicPlayer.stop()

	def previousSong(self):
		print("Previous")
		if self.EspeakEnabled:
			os.system("espeak Previous&")
		if self.SpotifyEnabled:
			self.MusicPlayer.previous()
			self.MusicPlayer.previous()

	def play(self):

		print("Toggle playing")
		if self.EspeakEnabled:
			os.system("espeak 'Toggle Playing'&")
		if self.SpotifyEnabled:
			print("here")
			self.MusicPlayer.play()

	def nextsong(self):
		print("Next")
		if self.EspeakEnabled:
			os.system("espeak Next&")
		if self.SpotifyEnabled:
			self.MusicPlayer.nextsong()

	def setLight(self,lightValue):
		print("Light "+str(lightValue))
		if self.WebGuiEnabled:
			self.Gui.emitLight(lightValue)

	def displayArtist(self,NameAndArtist):
		print("Displaying:  "+NameAndArtist)
		if self.WebGuiEnabled:
			self.Gui.emitNameAndArtist(NameAndArtist)



print __name__
if __name__ == '__main__':
	programm=MainUnit()





