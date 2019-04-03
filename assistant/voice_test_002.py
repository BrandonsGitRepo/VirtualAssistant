#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

import os
import urllib
import pyaudio
import pyttsx3
import requests
from random import randint
from bs4 import BeautifulSoup
import speech_recognition as sr
from lib.google_search_results import GoogleSearchResults


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')


def news_func(variant):
	"""
	gets news from news.google
	"""

	if variant is 0:

		url="https://news.google.com/?hl=en-GB&gl=GB&ceid=GB:en/"
		code=requests.get(url)
		soup=BeautifulSoup(code.text,'html5lib')

		news_article_headlines_raw = []
		for title in soup.find_all('span',class_=""):
			news_article_headlines_raw.append(title.text)

		clean_article_list = []
		for entry in news_article_headlines_raw:
			if "more_vert" in entry:
				continue
			else:
				clean_article_list.append(entry+'.')

		final_list = []
		for val in range(0,3):
			final_list.append(clean_article_list[randint(0,len(clean_article_list))])

		return clean_article_list, final_list

	elif variant is 1:

		url = "https://news.google.com/search?q=london&hl=en-GB&gl=GB&ceid=GB%3Aen"
		code=requests.get(url)
		soup=BeautifulSoup(code.text,'html5lib')

		news_article_headlines_raw = []
		for title in soup.find_all('span',class_=""):
			news_article_headlines_raw.append(title.text)

		clean_article_list = []
		for entry in news_article_headlines_raw:
			if "more_vert" in entry:
				continue
			else:
				clean_article_list.append(entry+'.')

		final_list = []
		for val in range(0,3):
			final_list.append(clean_article_list[randint(0,len(clean_article_list))])

		return clean_article_list, final_list


def friday_assistant(source):
	"""
	main assistant function
	"""
	audio = r.listen(source)
	user_req = r.recognize_google(audio)

	if "your name" in user_req:
		what_to_say = "My name is Friday"

		engine.say(what_to_say)
		engine.runAndWait()

	elif "what do you do" in user_req:
		what_to_say = "at the moment i only really give you random news headlines. and i can use google maps a little bit."

		engine.say(what_to_say)
		engine.runAndWait()

	elif "where is" in user_req:

		user_req = user_req.split(" ")
		user_req_len = len(user_req)

		if user_req_len <= 3:

			location = user_req[2]

			engine.say("Hold on, I will show you where " + location + " is.")
			engine.runAndWait()
			os.system("start chrome https://www.google.com/maps/dir//{0}/".format(location))

		elif user_req_len > 3:

			temp_user_req = user_req[2:]
			seperator = ''
			location = seperator.join(temp_user_req)

			engine.say("Hold on, I will show you where " + location + " is.")
			engine.runAndWait()
			os.system("start chrome https://www.google.com/maps/dir//{0}/".format(location))

		else:
			pass


	elif "news" in user_req:

		if "world" in user_req:
			variant = 0
			clean_article_list, final_list = news_func(variant)

			articlelen = len(clean_article_list)

			what_to_say = "There are {0} worldwide articles. im going to give you 3 random ones. {1}".format(articlelen, final_list)

			engine.say(what_to_say)
			engine.runAndWait()

		elif "London" in user_req:
			variant = 1
			clean_article_list, final_list = news_func(variant)

			articlelen = len(clean_article_list)

			what_to_say = "There are {0} articles regarding london. im going to give you 3 random ones. {1}".format(articlelen, final_list)

			engine.say(what_to_say)
			engine.runAndWait()

		else:
			pass

	elif "Friday stop" in user_req:
		what_to_say = "ok, going to sleep now. good bye"
		engine.say(what_to_say)
		engine.runAndWait()

		raise Exception(print('stopping'))

	else:
		print(user_req)
		misunderstood_string = "im sorry, i cant interpret {0} as a request yet. Please check the console for more details".format(user_req)
		engine.say(misunderstood_string)
		engine.runAndWait()
		print('*'*40)
		print('contact author or update my capabilities')
		print('*'*40)


if __name__ == '__main__':

	r=sr.Recognizer()
	r.energy_threshold=4000

	intro = "Hello, how may i help you"
	engine.say(intro)
	engine.runAndWait()

	with sr.Microphone() as source:
		while 1:
			friday_assistant(source)
