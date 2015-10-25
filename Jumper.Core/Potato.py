# -*- coding: utf-8 -*-
import os

from Point import *
from Key import *


class Potato():

	def __init__(self, screenCords, spriteManager, enviroment):
		self.__SPEED__ = Point(15, 45)
		self.__SPRITEMANAGER__ = spriteManager
		self.__SCREEN__ = screenCords
		self.__WIDTH__ = 30
		self.__HEIGHT__ = 30

		#self.ActualPosition = Point(30*8,30*8)
		startCord = enviroment.GetStartCords()
		self.ActualPosition = Point(startCord.X*30, startCord.Y*30)

		self.images = ['potatoStanding.png', 'potatoWalking.png', 'potatoJumping.png']
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.actualImageIndex = 0

		self.CreateSprite()

		self.maxJumping = self.__SPEED__.Y * 3
		self.startJumpingCord = self.ActualPosition.Y
		
	def GetImagePath(self, image):
		return os.path.join('..', 'Jumper.Core','Resources', image)

	def GetImageToShow(self):
		image = None
		if(self.isJumping | self.isGoingDown):
			self.actualImageIndex = 2
		elif(not self.isStanding):
			if(self.actualImageIndex > 1):
				self.actualImageIndex = 0
			else:
				self.actualImageIndex += 1
		else:
			self.actualImageIndex = 0

		return self.images[self.actualImageIndex]

	def GetSprite(self):
		return self.__SPRITEMANAGER__.GetSprite()

	def CreateSprite(self):
		imagePath = self.GetImagePath(self.images[0])

		self.__SPRITEMANAGER__.CreateSprite(self.ActualPosition.X, self.ActualPosition.Y,
			self.__WIDTH__, self.__HEIGHT__, imagePath)

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
		self.isStanding = True
		self.MoveOnXAxis(keysPressed)

		if(Key.Space in keysPressed):
			self.JumpInitialize()
			
		self.Jump()

		return self.UpdateSpritePosition()

	def MoveOnXAxis(self, keysPressed):
		if(Key.A in keysPressed):
			self.isStanding = False
			self.ActualPosition.X -= self.__SPEED__.X
			if(not self.isGoingLeft):
				self.isGoingLeft = True
		elif(Key.D in keysPressed):
			self.ActualPosition.X += self.__SPEED__.X
			self.isStanding = False
			if(self.isGoingLeft):
				self.isGoingLeft = False
		self.UpdateImage()

		self.StayOnScreen()

	def FlipSpriteImage(self):
		return self.__SPRITEMANAGER__.FlipSpriteImage()

	def StayOnScreen(self):
		if(self.ActualPosition.X < 0):
				self.ActualPosition.X = 0
		elif(self.ActualPosition.X > self.__SCREEN__.X - self.__WIDTH__):
				self.ActualPosition.X = self.__SCREEN__.X - self.__WIDTH__

	def UpdateImage(self):
		image = self.GetImageToShow()

		imagePath = self.GetImagePath(image)

		self.UpdateSpriteImage(imagePath)

		if(not self.isGoingLeft):
			self.FlipSpriteImage()

	def UpdateSpriteImage(self, imagePath):
		return self.__SPRITEMANAGER__.UpdateSpriteImage(imagePath)

	def UpdateSpritePosition(self):
		return self.__SPRITEMANAGER__.UpdateSprite(self.ActualPosition.X, self.ActualPosition.Y)