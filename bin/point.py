#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Point(object):

	def __init__(self, x=0, y=0):
		self.X = x
		self.Y = y

	def __str__(self):
		return "({0};{1})".format(self.X, self.Y)

	def __eq__(self, other):
		return self.X == other.X and self.Y == other.Y
		
	def __repr__(self):
		return "({0};{1})".format(self.X, self.Y)
