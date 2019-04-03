#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

import pyttsx3


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def speechResponse(fridays_response):
	"""
	runs fridays speech response
	"""
	engine=pyttsx3.init()
	engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
	engine.say(fridays_response)
	engine.runAndWait()
