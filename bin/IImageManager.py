#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IImageManager():

	def CreateImage(self, width, height, imagePath):
		raise NotImplementedError("Should have implemented this")

	def LoadImage(self, imagePath):
		raise NotImplementedError("Should have implemented this")

	def GetImage(self):
		raise NotImplementedError("Should have implemented this")

	def GetImageWidth(self):
		raise NotImplementedError("Should have implemented this")

	def GetImageHeight(self):
		raise NotImplementedError("Should have implemented this")

	def GetImageColor(self, r, g, b):
		raise NotImplementedError("Should have implemented this")

	def GetPixelArray(self):
		raise NotImplementedError("Should have implemented this")

	def GetPixelArrayItemColor(self, pixelArrayItem):
		raise NotImplementedError("Should have implemented this")