#!/usr/bin/env python
""" Application functions as a virtual assistant.
completeting tasks such as news browsing and maps
"""

import os
from responselib import speechResponse


__author__ = "Brandon Bailey"
__copyright__ = "Copyright 2019, Brandon Bailey"
__credits__ = ["Brandon Bailey"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Brandon Bailey"
__email__ = ""
__status__ = "Production"


def getMapLocation(usercommand):
	"""
	runs google maps in chrome on locations specified in usercommand
	"""
	usercommand = usercommand.split(" ")
	usercommand_len = len(usercommand)
	if usercommand_len <= 3:
		location = usercommand[2]
		fridays_response = "Hold on, I will show you where " + location + " is."
		speechResponse(fridays_response)
		os.system("start chrome https://www.google.com/maps/dir//{0}/".format(location))
	elif usercommand_len > 3:
		temp_usercommand = usercommand[2:]
		seperator = ''
		location = seperator.join(temp_usercommand)
		fridays_response = "Hold on, I will show you where " + location + " is."
		speechResponse(fridays_response)
		os.system("start chrome https://www.google.com/maps/dir//{0}/".format(location))
	else:
		pass
