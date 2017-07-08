#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import IImageManager


class PygameImageManager(IImageManager):

	def init(self):
		self._image = None

	def createImage(self, width, height, imagePath):
		image = pygame.image.load(imagePath)
		self._image = pygame.transform.scale(image, (width, height))
		return self._image

	def loadImage(self, imagePath):
		self._image = pygame.image.load(imagePath)

	def getImage(self):
		if(self._image is not None):
			return self._image
		else:
			raise Exception("Not loaded image")

	def getImageWidth(self):
		return self._image.get_width()

	def getImageHeight(self):
		return self._image.get_height()

	def getColor(self, r, g, b, a):
		return pygame.Color(r,g,b,a)

	def getPixelArray(self):
		return pygame.PixelArray(self._image)

	def getPixelArrayItemColor(self, pixelArrayItem):
		return pygame.Color(pixelArrayItem)
