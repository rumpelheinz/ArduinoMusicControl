import os
import re
from random import random

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit



def remove_quotes(string):
	return re.sub("'", "", string)

class WebGui:
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret!'
	mysocketio = SocketIO(app,async_mode='threading')

	@staticmethod
	@app.route('/')
	def index():
		print("index")
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Next')
	def mNext():
		print("Next")
		WebGui.MainUnit.nextsong()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Play')
	def mPlay():
		print("Play")
		WebGui.MainUnit.play()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Previous')
	def mPrevious():
		print("Previous")
		WebGui.MainUnit.previous()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Voice')
	def mVoice():
		print("Voice")
		WebGui.MainUnit.toggleVoice()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Whistle')
	def mWhistle():
		print("Whistle")
		WebGui.MainUnit.toggleWhistle()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Down')
	def mDown():
		print("Down")
		WebGui.MainUnit.lower()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])

	@staticmethod
	@app.route('/Louder')
	def mLouder():
		print("Louder")
		WebGui.MainUnit.louder()
		mint=int(round(random()*3))
		text=["http://www.animateit.net/data/media/189/2peng1.gif",
		"http://cdn.osxdaily.com/wp-content/uploads/2013/07/dancing-banana.gif",
		"http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-1.gif",
			  "http://bestanimations.com/Animals/Birds/Penguins/animated-penguin-gif-10.gif"]
		from random import randrange
		random_index = randrange(0,len(text))
		print text[random_index]

		return render_template('index.html',int=mint,mstring=text[random_index])



	@staticmethod
	@mysocketio.on('my broadcast event', namespace='/test')
	def test_message(message):
		your_string=message['data']
		your_string=remove_quotes(your_string)
		print(your_string)
		print("espeak '"+your_string+"'&")
		os.system("espeak '"+your_string+"'&")
		emit('my response', {'data': your_string}, broadcast=True)

	@staticmethod
	@mysocketio.on('connect', namespace='/test')
	def test_connect():
		artist=WebGui.MainUnit.getArtist()
		title=WebGui.MainUnit.getTitle()
		emit('music', {'data':artist+ " - "+title})
		emit('volume', {'data':WebGui.MainUnit.getVolume()})
		print(artist+ " - "+title)

	@staticmethod
	@mysocketio.on('mediabuttonevent', namespace='/test')
	def test_message(message):
		print("mediabutton")
		print(message['data'])
		if (message['data']=="previous"):
			WebGui.MainUnit.previous()
		elif (message['data']=="playpause"):
			WebGui.MainUnit.play()
		elif (message['data']=="next"):
			WebGui.MainUnit.nextsong()
		elif (message['data']=="louder"):
			WebGui.MainUnit.louder()
		elif (message['data']=="lower"):
			WebGui.MainUnit.lower()

	@staticmethod
	def emitVolume(volume):
		WebGui.mysocketio.emit('volume', {'data': volume }, namespace='/test')

	@staticmethod
	def emitLight(light):
		WebGui.mysocketio.emit('light', {'data': light }, namespace='/test')
	@staticmethod
	def emitNameAndArtist(NameAndArtist):
		WebGui.mysocketio.emit('music', {'data': NameAndArtist}, namespace='/test')


	def run(self,MainUnit):
		WebGui.MainUnit=MainUnit
		WebGui.mysocketio.run(self.app,debug=False, host='0.0.0.0')
