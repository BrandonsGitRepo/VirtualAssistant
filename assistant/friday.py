#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

from userinput import userspeech
from usercommandlib import commandRecognition
from responselib import speechResponse


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def friday():
	"""
	initializes friday
	"""
	user_speech = userspeech()
	commandRecognition(user_speech)

if __name__ == '__main__':
	speechResponse("Hello, how may I be of assistance?")
	while 1:
		friday()
