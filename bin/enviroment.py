#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point


class Enviroment(object):

	def __init__(self, starCords, checkpoint, tiles):
		self._starCords = starCords
		self._checkpoint = checkpoint
		self._tiles = tiles

	def getStartCords(self):
		return self._starCords

	def getCheckpoints(self):
		return self._checkpoint

	def getTiles(self):
		return self._tiles
