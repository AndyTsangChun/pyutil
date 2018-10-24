#! /usr/bin/env python

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class PyQueue():
	"""
	Queue with peek function
	"""
	# https://hg.python.org/cpython/file/2.7/Lib/Queue.py
	def __init__(self, maxsize=0):
		self.maxsize = maxsize
		self.queue = list()

	def peek(self):
		return (np.asarray(self.queue) if not self.empty() else [])

	def qsize(self):
		return len(self.queue)

	def empty(self):
		return len(self.queue) <= 0

	def full(self):
		return len(self.queue) >= self.maxsize

	def put(self, item):
		if self.full():
			self.get()
		self.queue.append(item)

	def get(self):
		if not self.empty():
			value = self.queue[0] 
			for i, item in enumerate(self.queue):
				if i != self.qsize() - 1:
					self.queue[i] = self.queue[i+1]
				else:
					self.queue.pop(i)

			return value
		else:
			return []