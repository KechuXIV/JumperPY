# -*- coding: utf-8 -*-
import os
import pygame

from Point import *


class Enviroment():

	def __init__(self):
		self.starCords = Point(0,0)
		self.finishCords = Point(0,0)
		self.tiles = [Point(1,2),Point(2,3)]

	def GetStartCords(self):
		return self.starCords

	def GetFinishCords(self):
		return self.finishCords

	def IsTile(self, point):
		return point in self.tiles