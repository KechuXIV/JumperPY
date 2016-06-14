#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point


class Enviroment(object):

	def __init__(self, starCords, finishCords, tiles):
		self.__starCords = starCords
		self.__finishCords = finishCords
		self.__tiles = tiles

	def getStartCords(self):
		return self.__starCords

	def getFinishCords(self):
		return self.__finishCords

	def isTile(self, point):
		return point in self.__tiles
