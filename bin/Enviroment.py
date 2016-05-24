#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from Point import *


class Enviroment():

	def __init__(self, starCords, finishCords, tiles):
		self.starCords = starCords
		self.finishCords = finishCords
		self.tiles = tiles

	def getStartCords(self):
		return self.starCords

	def getFinishCords(self):
		return self.finishCords

	def isTile(self, point):
		return point in self.tiles