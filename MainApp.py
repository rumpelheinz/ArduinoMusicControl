import os
from time import sleep

class MainUnit:
	print(__name__)

	ArduinoEnabled=True
	WhistleControlEnabled=False
	WebGuiEnabled=True
	SpotifyEnabled=True
	ListenerEnabled=True
	AlsaSoundEnabled=True
	VoiceRecognitionEnabled=False
	EspeakEnabled=True
	player="spotify"
	#player="banshee"



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

		self.MusicPlayer=MusicPlayer.MusicPlayer(self.player)

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
			self.arduinoReader=Arduino.ArduinoReader(self)
			self.arduinoReader.start()

		if self.WebGuiEnabled:
			print ("starting gui")
			self.Gui.run(self)

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

	def left(self):
		self.LampOff()
		print("Left room")
		if self.EspeakEnabled:
			os.system("espeak 'Left Room'&")
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")


	def entered (self):
		print("Entered room")
		if self.EspeakEnabled:
			self.LampOn()
			os.system("espeak 'Entered Room'&")
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play")



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
	def LampOn(self):
		self.arduinoReader.on()
	def LampOff(self):
		self.arduinoReader.off()

if __name__ == '__main__':
	programm=MainUnit()





