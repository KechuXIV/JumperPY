# -*- coding: utf-8 -*-


class ISpriteManager():

	def CreateImage(self, width, height, imagePath):
		raise NotImplementedError("Should have implemented this")

	def GetImage(self):
		raise NotImplementedError("Should have implemented this")