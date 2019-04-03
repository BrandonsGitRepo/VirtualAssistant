#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

import random
import requests
from bs4 import BeautifulSoup


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def headlineScrape(url):
	"""
	scrapes for headlines
	"""
	code = requests.get(url)
	soup = BeautifulSoup(code.text,'html5lib')
	headlines_raw = []
	for title in soup.find_all('span',class_=""):
		headlines_raw.append(title.text)
	headlines_clean = []
	for entry in headlines_raw:
		if "more_vert" in entry:
			continue
		else:
			headlines_clean.append(entry+'.')
	return headlines_clean

def getHeadLines(variant):
	"""
	gets news from news.google
	"""
	url = ["https://news.google.com/?hl=en-GB&gl=GB&ceid=GB:en/",
			"https://news.google.com/search?q=london&hl=en-GB&gl=GB&ceid=GB%3Aen"]
	if variant is 0:
		url = url[0]
		one_headline = "here is a random headline from the world . "
		one_headline += headlineScrape(url)[0]
		return one_headline
		#return headlineScrape(url)
	elif variant is 1:
		url = url[1]
		one_headline = "here is a random headline from london . "
		one_headline += headlineScrape(url)[0]
		return one_headline
		#return headlineScrape(url)
	else:
		pass
