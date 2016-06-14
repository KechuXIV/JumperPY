#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ISpriteManager(object):

	def createSprite(self, xPosition, yPosition, width, height, imagePath):
		raise NotImplementedError("Should have implemented this")

	def createSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		raise NotImplementedError("Should have implemented this")

	def getSprite(self):
		raise NotImplementedError("Should have implemented this")

	def flipSpriteImage(self):
		raise NotImplementedError("Should have implemented this")

	def updateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		raise NotImplementedError("Should have implemented this")

	def updateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		raise NotImplementedError("Should have implemented this")

	def updateSpriteImage(self, imagePath):
		raise NotImplementedError("Should have implemented this")
