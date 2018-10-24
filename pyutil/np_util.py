#! /usr/bin/env python

import io,os,sys
import numpy as np

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def npa2str(nparray):
	"""
	Convert a np.array to bytes string

	Args:
		nparray (np.array): numpy array
	Returns:
		**data** (string) - string data
	"""
	output = io.BytesIO()
	np.savez(output, x=nparray)
	data = output.getvalue()

	return data

def str2npa(s):
	"""
	Convert a bytes string to np.array

	Args:
		s (string): string data
	Returns:
		**nparray** (np.array) - numpy array
	"""
	return np.load(io.BytesIO(s))['x']

def sigmoid(x):
	"""
	Sigmoid operation

	Args:
		x(float): input X
	Return:
		**y** (float) - sigmoid(X)
	"""
	#if type(x) is not float and type(x) is not int:
	#	x = x.astype(dtype=np.float128)
	y = 1. / (1. + np.exp(-x))
	
	return y

def softmax(x, axis=-1, t=-100.):
	"""
	Softmax operation

	Args:
		x (numpy.array): input X
		axis (int): axis for sum
	Return:
		**softmax** (numpy.array) - softmax(X)
	"""
	x = x - np.max(x)
	if np.min(x) < t:
		x = x/np.min(x)*t
		
	e_x = np.exp(x)

	return e_x / e_x.sum(axis, keepdims=True)

# if __name__ == "__main__":
# 	x = np.arange(1280).reshape(128,10)
# 	print(x.dtype)
# 	print(x.tostring())
# 	s = npa2str(x)
# 	print(str2npa(s))

