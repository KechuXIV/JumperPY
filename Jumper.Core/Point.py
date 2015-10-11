# -*- coding: utf-8 -*-


class Point():

	def __init__(self, x=0, y=0):
		self.X = x
		self.Y = y

	def __str__(self):
		return "({0};{1})".format(self.X, self.Y)