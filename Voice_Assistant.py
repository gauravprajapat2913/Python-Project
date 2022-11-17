import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes
import os
import time


def sptext():
	recognizer=sr.Recognizer()
	with sr.Microphone() as source:
		speechtx("listening")
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		try:
			speechtx("recognizing")
			data = recognizer.recognize_google(audio)
			return data
		except sr.UnknownValueError:
			print(" Not Understand ")
			speechtx("not understand")
			time.sleep(2)
			return sptext()

def speechtx(x): # pip install pyttsx3==2.71
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[0].id)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine.say(x)
	engine.runAndWait()

if __name__ == '__main__':

			speechtx("hello lets start")
	 		while True :
	 				
	 				data1=sptext().lower()

	 				if "your name" in data1:
	 					name = " my name is peter"
	 					speechtx(name)
	 					continue

	 				elif "old are you" in data1:
	 					age = "i am two years old"
	 					speechtx(age)
	 					continue

	 				elif 'time' in data1:
	 					time = datetime.datetime.now().strftime("%I%M%p") # current time play
	 					speechtx(time)
	 					continue

	 				elif 'youtube' in data1:
	 					speechtx("open wscube tech youtube channel")
	 					webbrowser.open("https://www.youtube.com/c/wscubetechjodhpur") # youtube channel url

	 				elif 'web' in data1:
	 					speechtx("open wscube tech web")
	 					webbrowser.open("https://www.wscubetech.com/") # web page url

	 				elif "joke" in data1:
	 					joke_1 = pyjokes.get_joke(language="en",category="neutral")
	 					print(joke_1)
	 					speechtx(joke_1)
	 					continue

	 				elif 'play song' in data1:
	 					speechtx("system song and  youtube song ")
	 					ask = sptext().lower()

	 					if "youtube" in ask :
	 						webbrowser.open("https://www.youtube.com/watch?v=DyKjsL-6-Z8&ab_channel=jackson") # youtube song url 
	 					elif ("song" in ask) or ("folader" in ask): 
	 						try:
	 							add = "D:\gaurav\song" # song folder adderse address
	 							listsong = os.listdir(add)
	 							os.startfile(os.path.join(add,listsong[0])) # first song play
	 							# if you change song than change 0  
	 						except :
	 							speechtx("not song in folader")
	 							continue
	 					else :
	 						speechtx("wrong command")
	 						continue

	 				elif ("exit" in data1) or ("stop" in data1):
	 					speechtx("thank you")
	 					break
	 				else :
	 					speechtx("wrong command")
	 					continue

	 				time.sleep(5)
					
