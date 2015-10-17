# -*- coding: utf-8 -*-


class ISurfaceManager():

	def CreateSurface(self, width, height):
		raise NotImplementedError("Should have implemented this")

	def GetSurface(self):
		raise NotImplementedError("Should have implemented this")

	def BlitIntoSurface(self, image, width, height):
		raise NotImplementedError("Should have implemented this")	