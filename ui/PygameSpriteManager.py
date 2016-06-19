#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import ISpriteManager


class PygameSpriteManager(ISpriteManager):

	def __init__(self):
		self.__sprite = None
		self.__width = None
		self.__height = None

	def createSprite(self, xPosition, yPosition, width, height, surceface=None):
		if surceface is None:
			surceface = pygame.Surface([width, height], pygame.SRCALPHA, 32)

		self.__sprite = pygame.sprite.Sprite()
		self.__sprite.image = surceface
		self.__width = width
		self.__height = height
		self.__sprite.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self.__sprite

	def createSpriteFromImagePath(self, xPosition, yPosition, width, height, imagePath):
		surceface = pygame.transform.scale(pygame.image.load(imagePath), (width, height))
		self.createSpriteFromSurface(xPosition, yPosition, width, height, surceface)

		return self.__sprite

	def createSpriteFromSurface(self, xPosition, yPosition, width, height, surceface):
		self.__sprite = pygame.sprite.Sprite()
		self.__sprite.image = surceface
		self.__width = width
		self.__height = height
		self.__sprite.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self.__sprite

	def getSprite(self):
		sprite = None

		if(self.__sprite is not None):
			sprite = self.__sprite
		else:
			raise Exception("Not created sprite")
			
		return sprite

	def flipSpriteImage(self):
		self.__sprite.image = pygame.transform.flip(self.__sprite.image, True, False)

	def updateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		self.__sprite.rect.x = xPosition
		self.__sprite.rect.y = yPosition

		if(width is not None):
			raise NotImplementedError("Should have implemented this")
		if(height is not None):
			raise NotImplementedError("Should have implemented this")
		if(imagePath is not None):
			raise NotImplementedError("Should have implemented this")

		return self.__sprite

	def updateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		self.__sprite.rect.x = xPosition
		self.__sprite.rect.y = yPosition
		self.__sprite.image = sourceface
		self.__width = width
		self.__height = height

		return self.__sprite

	def updateSpriteImage(self, imagePath):
		self.__sprite.image = pygame.transform.scale(pygame.image.load(imagePath), (self.__width, self.__height))

		return self.__sprite