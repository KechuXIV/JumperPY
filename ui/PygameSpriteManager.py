#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from ISpriteManager import *


class PygameSpriteManager(ISpriteManager):

	def __init__(self):
		self.__sprite__ = None
		self.__width__ = None
		self.__height__ = None

	def createSprite(self, xPosition, yPosition, width, height, imagePath):
		sourceface = pygame.transform.scale(pygame.image.load(imagePath), (width, height))
		self.createSpriteFromSurface(xPosition, yPosition, width, height, sourceface)

		return self.__sprite__

	def createSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		self.__sprite__ = pygame.sprite.Sprite()
		self.__sprite__.image = sourceface
		self.__width__ = width
		self.__height__ = height
		self.__sprite__.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self.__sprite__

	def getSprite(self):
		sprite = None

		if(self.__sprite__ is not None):
			sprite = self.__sprite__
		else:
			raise Exception("Not created sprite")
			
		return sprite

	def flipSpriteImage(self):
		self.__sprite__.image = pygame.transform.flip(self.__sprite__.image, True, False)

	def updateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		self.__sprite__.rect.x = xPosition
		self.__sprite__.rect.y = yPosition

		if(width is not None):
			raise NotImplementedError("Should have implemented this")
		if(height is not None):
			raise NotImplementedError("Should have implemented this")
		if(imagePath is not None):
			raise NotImplementedError("Should have implemented this")

		return self.__sprite__

	def updateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		self.__sprite__.rect.x = xPosition
		self.__sprite__.rect.y = yPosition
		self.__sprite__.image = sourceface
		self.__width__ = width
		self.__height__ = height

		return self.__sprite__

	def updateSpriteImage(self, imagePath):
		self.__sprite__.image = pygame.transform.scale(pygame.image.load(imagePath), (self.__width__, self.__height__))

		return self.__sprite__