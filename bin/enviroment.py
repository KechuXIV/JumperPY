#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point


class Enviroment(object):

	def __init__(self, starCords, finishCords, tiles):
		self._starCords = starCords
		self._finishCords = finishCords
		self._tiles = tiles

	def getStartCords(self):
		return self._starCords

	def getFinishCords(self):
		return self._finishCords

	def isTile(self, point):
		return point in self._tiles
