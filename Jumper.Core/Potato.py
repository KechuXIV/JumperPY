# -*- coding: utf-8 -*-

import pygame
import os

from Point import *
from Key import *


class Potato():

	def __init__(self):
		self.__velocidadEnX__ = 30
		self.ActualPosition = Point(30,30)
		self.__sprite__ = pygame.sprite.Sprite()
		self.__sprite__.image = pygame.image.load(
			os.path.join('..', 'Jumper.Core','Resources','redbox.png'))

		self.__sprite__.rect = pygame.Rect(
			(self.ActualPosition.X, self.ActualPosition.Y), (30, 30))

	def Motion(self, key):
		if(key == Key.A):
			self.ActualPosition.X -= self.__velocidadEnX__
		elif(key == Key.D):
			self.ActualPosition.X += self.__velocidadEnX__

		self.__sprite__.rect.x = self.ActualPosition.X

	def GetSprite(self):
		return self.__sprite__