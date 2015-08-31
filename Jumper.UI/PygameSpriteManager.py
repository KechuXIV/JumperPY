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
		self.__width__ = None
		self.__height__ = None

	def CreateSprite(self, xPosition, yPosition, width, height, imagePath):
		self.__sprite__ = pygame.sprite.Sprite()
		self.__sprite__.image = pygame.transform.scale(pygame.image.load(imagePath), (width, height))
		self.__width__ = width
		self.__height__ = height
		self.__sprite__.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self.__sprite__

	def GetSprite(self):
		sprite = None

		if(self.__sprite__ is not None):
			sprite = self.__sprite__
		else:
			raise Exception("Not created sprite")
			
		return sprite

	def FlipSpriteImage(self):
		self.__sprite__.image = pygame.transform.flip(self.__sprite__.image, True, False)

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

	def UpdateSpriteImage(self, imagePath):
		self.__sprite__.image = pygame.transform.scale(pygame.image.load(imagePath), (self.__width__, self.__height__))

		return self.__sprite__