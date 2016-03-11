from dbus import DBusException
import dbus
from threading import Thread
import time




class Listener(Thread):
	def __init__(self,MainUnit):
		Thread.__init__(self)
		self.MainUnit=MainUnit

	def run(self):
		while True:
			try:
				bus = dbus.SessionBus()
				spotify_bus = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
				properties_interface = dbus.Interface(spotify_bus, 'org.freedesktop.DBus.Properties')
				while(True):
					info=properties_interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

					newartist=str(info['xesam:artist'][0].encode("utf-8"))
					newtitle=str(info['xesam:title'].encode("utf-8"))


					if (newtitle!=self.MainUnit.getTitle()):
						self.MainUnit.setChanged(True)
						self.MainUnit.setArtist(newartist)
						self.MainUnit.setTitle(newtitle)
						self.MainUnit.displayArtist(newartist+" - "+newtitle)
					time.sleep(1)
			except IndexError, e:
				print (str(e)+ ": Propably no song selected in Spotify.")
				self.MainUnit.play()
				time.sleep(2)

			except DBusException :
				print "DBusException : Spotify propably not open"
				time.sleep(2)
