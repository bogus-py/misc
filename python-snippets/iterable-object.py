#!/bin/env python

class itertest:
	def __init__(self, n):
		self.n = n
		self.counter = 0

	def __iter__(self):
		return self

	def next(self):
		if self.counter <= self.n:
			self.counter += 1
			return self.counter
		else:
			raise StopIteration

a = itertest(5)
for x in a:
	print x

