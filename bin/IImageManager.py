#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IImageManager(object):

	def createImage(self, width, height, imagePath):
		raise NotImplementedError("Should have implemented this")

	def loadImage(self, imagePath):
		raise NotImplementedError("Should have implemented this")

	def getImage(self):
		raise NotImplementedError("Should have implemented this")

	def getImageWidth(self):
		raise NotImplementedError("Should have implemented this")

	def getImageHeight(self):
		raise NotImplementedError("Should have implemented this")

	def getImageColor(self, r, g, b):
		raise NotImplementedError("Should have implemented this")

	def getPixelArray(self):
		raise NotImplementedError("Should have implemented this")

	def getPixelArrayItemColor(self, pixelArrayItem):
		raise NotImplementedError("Should have implemented this")
