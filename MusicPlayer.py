
import os
import alsaaudio




class MusicPlayer:
	def __init__(self,player):
		self.player=player


	def previous(self):
		print("MPrev")
		if (self.player=="spotify"):
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
		if self.player=="banshee":
			os.system("banshee --previous&")

	def play(self):
		print("MPlay")
		if (self.player=="spotify"):
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
		if self.player=="banshee":
			os.system("banshee --toggle-playing&")

	def nextsong(self):
		print("Mnext")
		if (self.player=="spotify"):
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
		if self.player=="banshee":
			os.system("banshee --next&")

	def stop(self):
		print("mStop")
		if (self.player=="spotify"):
			os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")
		if self.player=="banshee":
			os.system("banshee --pause&")


	def louder(self):
		m = alsaaudio.Mixer()
		m.setvolume(min(m.getvolume()[0]+5,100))

	def lower(self):
		m = alsaaudio.Mixer()
		m.setvolume(max(m.getvolume()[0]-5,0))

	def getVolume(self):
		m = alsaaudio.Mixer()
		return m.getvolume()[0]

	def setVolume(self,sound):
		m = alsaaudio.Mixer()
		m.setvolume(sound)






if __name__ == '__main__':
	from  Tkinter import *
	player=MusicPlayer("banshee")
	top = Tk()
	B = Button(top, text ="<", command = player.previous)
	B.pack(side=LEFT)
	B = Button(top, text ="||", command =  player.play)
	B.pack(side=LEFT)
	B = Button(top, text =">", command =  player.nextsong)
	B.pack(side=LEFT)
	B = Button(top, text ="+", command =  player.louder)
	B.pack(side=LEFT)
	B = Button(top, text ="-", command =  player.lower)
	B.pack(side=LEFT)
	B = Button(top, text ="X", command =  player.stop)
	B.pack(side=LEFT)
# Code to add widgets will go here...
	top.mainloop()

