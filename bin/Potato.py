#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point, Key


class Potato(object):

	def __init__(self, screenCords, spriteManager, enviroment, soundManager, tracer):
		self.__SPEED__ = Point(4, 6)
		self.__spriteManager__ = spriteManager
		self.__screen__ = screenCords
		self.__width__ = 30
		self.__height__ = 30
		self.__enviroment__ = enviroment
		self.__tracer__ = tracer

		self.setPotatoOnStartPosition()

		self.images = ['potatoStanding.png', 'potatoWalking.png', 'potatoJumping.png']
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0

		self.deathSound = soundManager.getSound(os.path.join('..', 'bin','Resources', 'sounds', 'death.wav'))
		self.jumpSound = soundManager.getSound(os.path.join('..', 'bin','Resources', 'sounds', 'jump.wav'))
		self.checkpointSound = soundManager.getSound(os.path.join('..', 'bin','Resources', 'sounds', 'checkpoint.wav'))

		self.createSprite()
		
	def getImagePath(self, image):
		return os.path.join('..', 'bin','Resources', image)

	def getImageToShow(self):
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

	def getSprite(self):
		return self.__spriteManager__.getSprite()

	def createSprite(self):
		imagePath = self.getImagePath(self.images[0])

		self.__spriteManager__.createSprite(self.ActualPosition.X, self.ActualPosition.Y,
			self.__width__, self.__height__, imagePath)

	def endjumpCycle(self):
		self.isJumping = False
		self.isGoingDown = False

	def flipSpriteImage(self):
		return self.__spriteManager__.flipSpriteImage()

	def jump(self):
		if(self.isJumping):
			if(self.isGoingDown):
				self.ActualPosition.Y += self.__SPEED__.Y
				self.__SPEED__.Y += 0.4
			else:
				if(self.__SPEED__.Y <= 0):
					self.isGoingDown = True
				else:
					self.ActualPosition.Y -= self.__SPEED__.Y
					self.__SPEED__.Y -= 0.4

			if(self.thereIsTileBehind() and self.isGoingDown):
				self.endjumpCycle()
				self.stabilizeYPosition()
			else:
				if(self.ActualPosition.Y >= self.__screen__.Y):
					self.endjumpCycle()
					self.deathSound.play()
					self.setPotatoOnStartPosition()
					self.isStanding = True

	def jumpInitialize(self):
		if(not self.isJumping):
			self.jumpSound.play()
			self.isStanding = False
			self.isJumping = True
			self.__SPEED__.Y = 8

	def motion(self, keysPressed):
		self.isStanding = True
		if(Key.Space in keysPressed):
			self.jumpInitialize()

		self.moveOnXAxis(keysPressed)
		self.moveOnYAxis()
	
		self.jump()
		return self.updateSpritePosition()

	def moveOnXAxis(self, keysPressed):
		if(Key.A in keysPressed):
			self.isStanding = False
			self.isGoingLeft = True
			if(not self.thereIsTileLeft()):
				self.ActualPosition.X -= self.__SPEED__.X
				
		elif(Key.D in keysPressed):
			self.isStanding = False
			self.isGoingLeft = False
			if(not self.thereIsTileRight()):
				self.ActualPosition.X += self.__SPEED__.X
				
		self.hasReachCheckpoint()
		self.updateImage()

		self.stayOnScreen()

	def moveOnYAxis(self):
		if((not self.isJumping) and (not self.thereIsTileBehind())):
			self.jumpInitialize()
			self.isGoingDown = True

	def newLevel(self, enviroment):
		self.__enviroment__ = enviroment

		self.setPotatoOnStartPosition()
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0

	def hasReachCheckpoint(self):
		actualCord = Point(round(self.ActualPosition.X/30), round(self.ActualPosition.Y/30))
		self.reachCheckpoint = actualCord == self.__enviroment__.getFinishCords()
		if(self.reachCheckpoint):
			self.checkpointSound.play()

	def setPotatoOnStartPosition(self):
		startCord = self.__enviroment__.getStartCords()
		self.setActualPosition(startCord)

	def setActualPosition(self, point):
		self.ActualPosition = Point(point.X*30, point.Y*30)

	def stabilizeYPosition(self):
		self.ActualPosition.Y = round(self.ActualPosition.Y/30) * 30

	def stayOnScreen(self):
		if(self.ActualPosition.X < 0):
			self.ActualPosition.X = self.__screen__.X
		elif(self.ActualPosition.X > self.__screen__.X):
			self.ActualPosition.X = 0

	def thereIsTileBehind(self):
		behindPosition = Point(round((self.ActualPosition.X+10)/30), round(self.ActualPosition.Y/30) + 1)
		isTileBehind = self.__enviroment__.isTile(behindPosition)
		self.__tracer__.push("ActualPosition: {0}\n\rBehindPosition: {1}\n\risTileBehind: {2}",
			self.ActualPosition, behindPosition, isTileBehind)
		return isTileBehind
		
	def thereIsTileLeft(self):
		leftPosition = Point(round((self.ActualPosition.X-2)/30), round(self.ActualPosition.Y/30))
		isTileLeft = self.__enviroment__.isTile(leftPosition)
		self.__tracer__.push("ActualPosition: {0}\n\rLeftPosition: {1}\n\rIsTileLeft: {2}",
			self.ActualPosition, leftPosition, isTileLeft)
		return isTileLeft
		
	def thereIsTileRight(self):
		rightPosition = Point(round((self.ActualPosition.X/30)) + 1, round(self.ActualPosition.Y/30))
		isTileRight = self.__enviroment__.isTile(rightPosition)
		self.__tracer__.push("ActualPosition: {0}\n\rRightPosition: {1}\n\rIsTileRight: {2}",
			self.ActualPosition, rightPosition, isTileRight)
		return isTileRight

	def updateImage(self):
		image = self.getImageToShow()
		
		imagePath = self.getImagePath(image)

		self.updateSpriteImage(imagePath)

		if(not self.isGoingLeft):
			self.flipSpriteImage()

	def updateSpriteImage(self, imagePath):
		return self.__spriteManager__.updateSpriteImage(imagePath)

	def updateSpritePosition(self):
		return self.__spriteManager__.updateSprite(self.ActualPosition.X, self.ActualPosition.Y)