# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from IImageManager import *


class ImageManager():

	def __init__(self):
		self.__image__ = None

	def CreateImage(self, width, height, imagePath):
		image = pygame.image.load(imagePath)
		self.__image__ = pygame.transform.scale(image, (width, height))
		return self.__image__

	def GetImage(self):
		if(self.__image__ is not None):
			return self.__image__
		else:
			raise Exception("Not created image")