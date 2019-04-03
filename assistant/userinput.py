#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

import speech_recognition as sr


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def userspeech():
	"""
	recrods audio input and returns output
	"""
	r=sr.Recognizer()
	r.energy_threshold=4000
	with sr.Microphone() as userspeech:
		audio=r.listen(userspeech)
		output=r.recognize_google(audio)
		return output
