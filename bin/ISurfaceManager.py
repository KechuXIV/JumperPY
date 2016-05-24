#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ISurfaceManager():

	def createSurface(self, width, height):
		raise NotImplementedError("Should have implemented this")

	def getSurface(self):
		raise NotImplementedError("Should have implemented this")

	def blitIntoSurface(self, image, width, height):
		raise NotImplementedError("Should have implemented this")	