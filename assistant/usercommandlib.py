#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

from userinput import userspeech
from newslib import getHeadLines
from gmapslib import getMapLocation
from responselib import speechResponse


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def commandRecognition(userspeech):
	"""
	recognises command and activates appropriate response
	"""
	if "your name" in userspeech:
		speechResponse("my name is Friday.")
	elif "what do you do" in userspeech:
		speechResponse("im currently not sure. my libraries are a bit jumbled up. Something to do with google maps and the news.")
	elif "where is" in userspeech:
		getMapLocation(userspeech)
	elif "news" in userspeech:
		if "world" in userspeech:
			variant = 0
			speechResponse(getHeadLines(variant))
		elif "London" in userspeech:
			variant = 1
			speechResponse(getHeadLines(variant))
		else:
			pass
	elif "Friday stop" in userspeech:
		speechResponse("ok. going to sleep.")
		raise Exception(print('stopping'))
	else:
		pass
