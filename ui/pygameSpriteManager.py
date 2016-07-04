#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import ISpriteManager


class PygameSpriteManager(ISpriteManager):

	def __init__(self):
		self._sprite = None
		self._width = None
		self._height = None

	def createSprite(self, xPosition, yPosition, width, height, surceface=None):
		if surceface is None:
			surceface = pygame.Surface([width, height], pygame.SRCALPHA, 32)

		self._sprite = pygame.sprite.Sprite()
		self._sprite.image = surceface
		self._width = width
		self._height = height
		self._sprite.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self._sprite

	def createSpriteFromImagePath(self, xPosition, yPosition, width, height, imagePath):
		surceface = pygame.transform.scale(pygame.image.load(imagePath), (width, height))
		self.createSpriteFromSurface(xPosition, yPosition, width, height, surceface)

		return self._sprite

	def createSpriteFromSurface(self, xPosition, yPosition, width, height, surceface):
		self._sprite = pygame.sprite.Sprite()
		self._sprite.image = surceface
		self._width = width
		self._height = height
		self._sprite.rect = pygame.Rect((xPosition, yPosition), (width, height))

		return self._sprite

	def getSprite(self):
		sprite = None

		if(self._sprite is not None):
			sprite = self._sprite
		else:
			raise Exception("Not created sprite")
			
		return sprite

	def flipSpriteImage(self):
		self._sprite.image = pygame.transform.flip(self._sprite.image, True, False)

	def updateSprite(self, xPosition, yPosition, width = None, height = None, imagePath = None):
		self._sprite.rect.x = xPosition
		self._sprite.rect.y = yPosition

		if(width is not None):
			raise NotImplementedError("Should have implemented this")
		if(height is not None):
			raise NotImplementedError("Should have implemented this")
		if(imagePath is not None):
			raise NotImplementedError("Should have implemented this")

		return self._sprite

	def updateSpriteFromSurface(self, xPosition, yPosition, width, height, sourceface):
		self._sprite.rect.x = xPosition
		self._sprite.rect.y = yPosition
		self._sprite.image = sourceface
		self._width = width
		self._height = height

		return self._sprite

	def updateSpriteImage(self, imagePath):
		self._sprite.image = pygame.transform.scale(pygame.image.load(imagePath), (self._width, self._height))

		return self._sprite
