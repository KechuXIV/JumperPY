# -*- coding: utf-8 -*-

import pygame
import os

from Point import *
from Key import *


class Potato():

	def __init__(self):
		self.__SPEED__ = Point(30, 45)

		self.ActualPosition = Point(30*8,30*8)
		self.InitializeSprite()

		self.isJumping = False
		self.isGoingDown = False
		self.maxJumping = self.__SPEED__.Y * 3
		self.startJumpingCord = self.ActualPosition.Y
		

	def GetSprite(self):
		return self.__sprite__

	def InitializeSprite(self):
		self.__sprite__ = pygame.sprite.Sprite()
		self.__sprite__.image = pygame.image.load(
			os.path.join('..', 'Jumper.Core','Resources','redbox.png'))
		self.__sprite__.rect = pygame.Rect(
			(self.ActualPosition.X, self.ActualPosition.Y), (30, 30))

	def Jump(self):
		if(self.isJumping):
			if(self.isGoingDown):
				self.ActualPosition.Y += self.__SPEED__.Y
			else:
				self.ActualPosition.Y -= self.__SPEED__.Y

			if(self.ActualPosition.Y <= self.maxJumping):
				self.isGoingDown = True

			if(self.ActualPosition.Y >= self.startJumpingCord):
				self.ActualPosition.Y = self.startJumpingCord
				self.isJumping = False
				self.isGoingDown = False

	def JumpInitialize(self):
		if(not self.isJumping):
			self.startJumpingCord = self.ActualPosition.Y
			self.isJumping = True

	def Motion(self, keysPressed):
		if(Key.A in keysPressed):
			self.ActualPosition.X -= self.__SPEED__.X
		elif(Key.D in keysPressed):
			self.ActualPosition.X += self.__SPEED__.X

		if(Key.Space in keysPressed):
			self.JumpInitialize()
			
		self.Jump()

		return self.UpdateSpritePosition()

	def UpdateSpritePosition(self):
		self.__sprite__.rect.x = self.ActualPosition.X
		self.__sprite__.rect.y = self.ActualPosition.Y

		return self.__sprite__