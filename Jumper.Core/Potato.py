# -*- coding: utf-8 -*-
import os

from Point import *
from Key import *


class Potato():

	def __init__(self, screenCords, spriteManager, enviroment, soundManager):
		self.__SPEED__ = Point(15, 30)
		self.__SPRITEMANAGER__ = spriteManager
		self.__SCREEN__ = screenCords
		self.__WIDTH__ = 30
		self.__HEIGHT__ = 30
		self.__ENVIROMENT__ = enviroment

		startCord = self.__ENVIROMENT__.GetStartCords()
		self.ActualPosition = Point(startCord.X*30, startCord.Y*30)

		self.images = ['potatoStanding.png', 'potatoWalking.png', 'potatoJumping.png']
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0

		self.deathSound = soundManager.GetSound(os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav'))
		self.jumpSound = soundManager.GetSound(os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav'))
		self.checkpointSound = soundManager.GetSound(os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav'))

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
		self.isJumping = False
		self.isGoingDown = False

	def FlipSpriteImage(self):
		return self.__SPRITEMANAGER__.FlipSpriteImage()

	def Jump(self):
		if(self.isJumping):
			if(self.isGoingDown):
				self.ActualPosition.Y += self.__SPEED__.Y
			else:
				self.ActualPosition.Y -= self.__SPEED__.Y

			if(self.ThereIsTileBehind()):
				self.EndJumpCycle()
			else:
				if(abs(self.ActualPosition.Y - self.startJumpingCord) >= self.maxJumping):
					if(self.ActualPosition.Y >= self.__SCREEN__.Y):
						self.EndJumpCycle()
						startCord = self.__ENVIROMENT__.GetStartCords()
						self.ActualPosition = Point(startCord.X*30, startCord.Y*30)
						self.deathSound.play()
						self.isStanding = True
					else:
						self.isGoingDown = True

	def JumpInitialize(self):
		if(not self.isJumping):
			self.jumpSound.play()
			self.startJumpingCord = self.ActualPosition.Y
			self.isStanding = False
			self.isJumping = True

	def Motion(self, keysPressed):
		self.isStanding = True
		if(Key.Space in keysPressed):
			self.JumpInitialize()

		self.MoveOnXAxis(keysPressed)
		self.MoveOnYAxis()
	
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
		
		self.ReachCheckpoint()
		self.UpdateImage()

		self.StayOnScreen()

	def MoveOnYAxis(self):
		if((not self.isJumping) and (not self.ThereIsTileBehind())):
			self.JumpInitialize()
			self.isGoingDown = True

	def NewLevel(self, enviroment):
		self.__ENVIROMENT__ = enviroment

		startCord = self.__ENVIROMENT__.GetStartCords()
		self.ActualPosition = Point(startCord.X*30, startCord.Y*30)
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0

	def ReachCheckpoint(self):
		actualCord = Point(abs(self.ActualPosition.X/30), abs(self.ActualPosition.Y/30))
		self.reachCheckpoint = actualCord == self.__ENVIROMENT__.GetFinishCords()
		if(self.reachCheckpoint):
			self.checkpointSound.play()
			

	def SetActualPosition(self, point):
		self.ActualPosition = Point(point.X*30, point.Y*30)

	def StayOnScreen(self):
		if(self.ActualPosition.X < 0):
			self.ActualPosition.X = self.__SCREEN__.X
		elif(self.ActualPosition.X > self.__SCREEN__.X):
			self.ActualPosition.X = 0

	def ThereIsTileBehind(self):
		behindPosition = Point(abs(self.ActualPosition.X/30), abs(self.ActualPosition.Y/30) + 1)
		return self.__ENVIROMENT__.IsTile(behindPosition)

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