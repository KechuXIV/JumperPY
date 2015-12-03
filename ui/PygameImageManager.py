#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from IImageManager import *


class PygameImageManager(IImageManager):

	def __init__(self):
		self.__image__ = None

	def CreateImage(self, width, height, imagePath):
		image = pygame.image.load(imagePath)
		self.__image__ = pygame.transform.scale(image, (width, height))
		return self.__image__

	def LoadImage(self, imagePath):
		self.__image__ = pygame.image.load(imagePath)

	def GetImage(self):
		if(self.__image__ is not None):
			return self.__image__
		else:
			raise Exception("Not loaded image")

	def GetImageWidth(self):
		return self.__image__.get_width()

	def GetImageHeight(self):
		return self.__image__.get_height()

	def GetImageColor(self, r, g, b):
		mapRGB = self.__image__.map_rgb((r, g, b))
		return pygame.Color(mapRGB)

	def GetPixelArray(self):
		return pygame.PixelArray(self.__image__)

	def GetPixelArrayItemColor(self, pixelArrayItem):
		return pygame.Color(pixelArrayItem)