# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from ISpriteManager import *

class PygameSpriteManager(ISpriteManager):

	def __init__(self):
		self.__sprite__ = None

	def CreateSprite(self, xPosition, yPosition, width, height, imagePath):
		self.__sprite__ = pygame.sprite.Sprite()
		self.__sprite__.image = pygame.image.load(imagePath)
		self.__sprite__.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self.__sprite__

	def GetSprite(self):
		sprite = None

		if(self.__sprite__ is not None):
			sprite = self.__sprite__
		else:
			raise Exception("Not created sprite")
			
		return sprite

	def UpdateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		self.__sprite__.rect.x = xPosition
		self.__sprite__.rect.y = yPosition

		if(width is not None):
			raise NotImplementedError("Should have implemented this")
		if(height is not None):
			raise NotImplementedError("Should have implemented this")
		if(imagePath is not None):
			raise NotImplementedError("Should have implemented this")

		return self.__sprite__