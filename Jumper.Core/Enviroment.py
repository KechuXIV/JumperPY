# -*- coding: utf-8 -*-
import os

from Point import *


class Enviroment():

	def __init__(self, starCords, finishCords, tiles):
		self.starCords = starCords
		self.finishCords = finishCords
		self.tiles = tiles

	def GetStartCords(self):
		return self.starCords

	def GetFinishCords(self):
		return self.finishCords

	def IsTile(self, point):
		return point in self.tiles