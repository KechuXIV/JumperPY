# -*- coding: utf-8 -*-

import pygame
import os

from Point import *
from Key import *


class Potato():

	def __init__(self, screenCords, spriteManager):
		self.__SPEED__ = Point(30, 45)
		self.__SPRITEMANAGER__ = spriteManager
		self.__SCREEN__ = screenCords

		self.ActualPosition = Point(30*8,30*8)
		self.CreateSprite()

		self.isJumping = False
		self.isGoingDown = False
		self.maxJumping = self.__SPEED__.Y * 3
		self.startJumpingCord = self.ActualPosition.Y
		

	def GetSprite(self):
		return self.__SPRITEMANAGER__.GetSprite()

	def CreateSprite(self):
		imagePath = os.path.join('..', 'Jumper.Core','Resources','redbox.png')
		width = 30
		height = 30

		self.__SPRITEMANAGER__.CreateSprite(self.ActualPosition.X, self.ActualPosition.Y,
			width, height, imagePath)

	def EndJumpCycle(self):
		self.ActualPosition.Y = self.startJumpingCord
		self.isJumping = False
		self.isGoingDown = False

	def Jump(self):
		if(self.isJumping):
			if(self.isGoingDown):
				self.ActualPosition.Y += self.__SPEED__.Y
			else:
				self.ActualPosition.Y -= self.__SPEED__.Y

			if(self.ActualPosition.Y <= self.maxJumping):
				self.isGoingDown = True

			if(self.ActualPosition.Y >= self.startJumpingCord):
				self.EndJumpCycle()

	def JumpInitialize(self):
		if(not self.isJumping):
			self.startJumpingCord = self.ActualPosition.Y
			self.isJumping = True

	def Motion(self, keysPressed):
		self.MoveOnXAxis(keysPressed)

		if(Key.Space in keysPressed):
			self.JumpInitialize()
			
		self.Jump()

		return self.UpdateSpritePosition()

	def MoveOnXAxis(self, keysPressed):
		if(Key.A in keysPressed):
			self.ActualPosition.X -= self.__SPEED__.X
		elif(Key.D in keysPressed):
			self.ActualPosition.X += self.__SPEED__.X

		self.StayOnScreen()

	def StayOnScreen(self):
		if(self.ActualPosition.X < 0):
				self.ActualPosition.X = 0
		elif(self.ActualPosition.X > self.__SCREEN__.X - self.__SPEED__.X):
				self.ActualPosition.X = self.__SCREEN__.X - self.__SPEED__.X

	def UpdateSpritePosition(self):
		return self.__SPRITEMANAGER__.UpdateSprite(self.ActualPosition.X, self.ActualPosition.Y)