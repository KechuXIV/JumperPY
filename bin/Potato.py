#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from Point import *
from Key import *


class Potato():

	def __init__(self, screenCords, spriteManager, enviroment, soundManager):
		self.__SPEED__ = Point(2, 8)
		self.__SPRITEMANAGER__ = spriteManager
		self.__SCREEN__ = screenCords
		self.__WIDTH__ = 30
		self.__HEIGHT__ = 30
		self.__ENVIROMENT__ = enviroment

		self.setPotatoOnStartPosition()

		self.images = ['potatoStanding.png', 'potatoWalking.png', 'potatojumping.png']
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
		return self.__SPRITEMANAGER__.getSprite()

	def createSprite(self):
		imagePath = self.getImagePath(self.images[0])

		self.__SPRITEMANAGER__.createSprite(self.ActualPosition.X, self.ActualPosition.Y,
			self.__WIDTH__, self.__HEIGHT__, imagePath)

	def endjumpCycle(self):
		self.isJumping = False
		self.isGoingDown = False

	def flipSpriteImage(self):
		return self.__SPRITEMANAGER__.flipSpriteImage()

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
				if(self.ActualPosition.Y >= self.__SCREEN__.Y):
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
			if(not self.isGoingLeft):
				self.isGoingLeft = True
			if(not self.thereIsTileLeft()):
				self.ActualPosition.X -= self.__SPEED__.X
				
		elif(Key.D in keysPressed):
			self.isStanding = False
			if(self.isGoingLeft):
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
		self.__ENVIROMENT__ = enviroment

		self.setPotatoOnStartPosition()
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0

	def hasReachCheckpoint(self):
		actualCord = Point(abs(self.ActualPosition.X/30), abs(self.ActualPosition.Y/30))
		self.reachCheckpoint = actualCord == self.__ENVIROMENT__.getFinishCords()
		if(self.reachCheckpoint):
			self.checkpointSound.play()

	def setPotatoOnStartPosition(self):
		startCord = self.__ENVIROMENT__.getStartCords()
		self.setActualPosition(startCord)

	def setActualPosition(self, point):
		self.ActualPosition = Point(point.X*30, point.Y*30)

	def stabilizeYPosition(self):
		self.ActualPosition.Y = round(self.ActualPosition.Y/30) * 30

	def stayOnScreen(self):
		if(self.ActualPosition.X < 0):
			self.ActualPosition.X = self.__SCREEN__.X
		elif(self.ActualPosition.X > self.__SCREEN__.X):
			self.ActualPosition.X = 0

	def thereIsTileBehind(self):
		behindPosition = Point(round(self.ActualPosition.X/30), round(self.ActualPosition.Y/30) + 1)
		isTileBehind = self.__ENVIROMENT__.isTile(behindPosition)
		print ("isTileBehind: {0}".format(isTileBehind))
		return isTileBehind
		
	def thereIsTileLeft(self):
		leftPosition = Point(round(self.ActualPosition.X/30) + 1, round(self.ActualPosition.Y/30))
		isTileLeft = self.__ENVIROMENT__.isTile(leftPosition)
		print ("isTileLeft: {0}".format(isTileLeft))
		return isTileLeft
		
	def thereIsTileRight(self):
		rightPosition = Point(round((self.ActualPosition.X/30)) - 1, round(self.ActualPosition.Y/30))
		isTileRight = self.__ENVIROMENT__.isTile(rightPosition)
		print ("isTileRight: {0}".format(isTileRight))
		return isTileRight

	def updateImage(self):
		image = self.getImageToShow()
		
		imagePath = self.getImagePath(image)

		self.updateSpriteImage(imagePath)

		if(not self.isGoingLeft):
			self.flipSpriteImage()

	def updateSpriteImage(self, imagePath):
		return self.__SPRITEMANAGER__.updateSpriteImage(imagePath)

	def updateSpritePosition(self):
		return self.__SPRITEMANAGER__.updateSprite(self.ActualPosition.X, self.ActualPosition.Y)