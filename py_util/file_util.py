#! /usr/bin/env python
import os,sys
import glob
import csv
import numpy as np
from numpy import genfromtxt

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def checkCreate(path):
	"""
	Check is directory exists, if not create it
	
	Args:
		path (string): directory path
	"""
	if not checkExists(path):
		os.makedirs(path)	

def checkExists(path):
	"""
	Check is directory exists
	
	Args:
		path (string): directory path
	Returns:
		**boolean** (boolean) - is directory exists
	"""
	return os.path.exists(path)

def checkCreateFile(path):
	"""
	Check is file exists, if not create that file
	
	Args:
		path (string): file path
	"""
	try:
		os.stat(path)
	except:
		with open(path, "w"):
			pass

def loadCSV(path, isNumpy=False):
	"""
	Load .csv file and return a list/np.array
	
	Args:
		path (string): file path
		isNumpy (boolean): return numpy array or list
	Returns:
		**data** (list) - list of data from .csv
	"""
	data = list()
	if isNumpy:
		if checkExists(path):
			data = genfromtxt(path, delimiter=',', dtype=str)
			# handle np.genfromtxt return different sized array if only have one entry
			if data.ndim == 1:
				data = np.array([data])
	else:
		if checkExists(path):
			with open(path, 'r') as csvfile:
				reader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				for row in reader:
					data.append(row)
	return data

def writeCSV(path, data):
	"""
	Write list/np.array into a csv

	np.savetxt() can adapt to list and np.array itself

	Args:
		path (string): file path
		data (list): list of data from .csv
	Returns:
		**op** (boolean) - operation result
	"""
	try:
		np.savetxt(path, data, delimiter=',', fmt="%s")
		# with open(path, 'a') as csvfile:
		# 	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		# 	writer.writerow(data)
		return True

	except Exception as e:
		print("[Err] ",e)
		return False

def getAllFiles(path, ext):
	"""
	Get all file with given extension in given path
	
	Args:
		path (string): file path
		ext (list): list of extension in string
	Returns:
		**files** (list) - list of file name
	"""
	sys_path = os.getcwd()
	if checkExists(path):
		files = list()
		os.chdir(path)
		for e in ext:
			files += glob.glob("*."+e)
		os.chdir(sys_path)
		return files		
	else:
		return None

