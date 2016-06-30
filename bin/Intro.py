#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import resourcePath as rs

from . import Point, Key

class Intro(object):

	def __init__(self, screen, spriteManager):
		self._screen = screen
		self._spriteManager = spriteManager
		self._imagePath = rs.INTRO_IMAGE
		self.gameStart = False

		self._createSprite()

	def _createSprite(self):
		self._spriteManager.createSpriteFromImagePath(0, 0,
			self._screen.X, self._screen.Y, self._imagePath)

	def getSprite(self):
		return self._spriteManager.getSprite()
