#! /usr/bin/env python
from sys import platform
from screeninfo import Monitor

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.1"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def getScreenInfo():
	"""
	Return screen width and height, not tested on Window yet
	
	Returns:
		**screen_info** (list) - list of screeninfo.Monitor
	"""
	if platform == "darwin":
		# screeninfo in osx requires pyobjus, which does not have pip installation
		# hence, we use AppKit instead, to use AppKit we need pyobjc
		from AppKit import NSScreen as ns
		screen_info = list()
		for screen in ns.screens():
			m = Monitor(screen.frame().origin.x, screen.frame().origin.y, screen.frame().size.width, screen.frame().size.height)
			screen_info.append(m)

		return screen_info

	elif platform == "linux":
		from screeninfo import get_monitors
		
		return get_monitors()
	elif platform == "window":
		# currently return single monitor only, need to be modify to get multiple window
		from win32api import GetSystemMetrics
		x = 0
		y = 0
		return [Monitor(x, y, GetSystemMetrics(0), GetSystemMetrics(1))]
	else:
		raise NotImplementedError("This environment is not supported.")