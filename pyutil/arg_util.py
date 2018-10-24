#! /usr/bin/env python
import argparse

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def str2bool(s):
	"""
	Convert string to Boolean
	
	Args:
		s (string): string
	Returns:
		**boolean** (boolean) - boolean
	"""
	if s.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif s.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')

def basic_args(parser):
	"""
	Initialize parser with basic arguments.
	
	Args:
		parser (ArgumentParser): Parser wish to add basic arguments
	Returns:
		**parser** (ArgumentParser) - Parser after modification
	"""
	parser.add_argument("-sl", "--showLog", type=str2bool, nargs='?',
						const=True, default=False,
						help="Enable to display Log.")
	parser.add_argument("-dbug", "--debugMode", type=str2bool, nargs="?",
						const=True, default=False,
						help="Enable debug mode.")

	return parser