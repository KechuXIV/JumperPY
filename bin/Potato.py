#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point, Key, resourcePath as rs


class Potato(object):

	def __init__(self, screenCords, spriteManager, enviroment, soundManager, tracer):
		self.__speed = Point(4, 6)
		self.__measure = Point(30, 30)
		self.__screen = screenCords
		self.__spriteManager = spriteManager
		self.__soundManager = soundManager
		self.__tracer = tracer
		self.__enviroment = enviroment

		self.__images = [rs.POTATO_STANDING, rs.POTATO_WALKING, rs.POTATO_JUMPING]
		self.__deathSound = self.getSound(rs.POTATO_DEATHSOUND)
		self.__jumpSound = self.getSound(rs.POTATO_JUMPSOUND)
		self.__checkpointSound = self.getSound(rs.POTATO_CHECKPOINTSOUND)

		self.setPotatoOnStartPosition()
		self.createSprite()

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

		return self.__images[self.actualImageIndex]

	def getSound(self, path):
		return self.__soundManager.getSound(path)

	def getSprite(self):
		return self.__spriteManager.getSprite()

	def createSprite(self):
		self.__spriteManager.createSprite(self.ActualPosition.X, self.ActualPosition.Y,
			self.__measure.X, self.__measure.Y)

	def endjumpCycle(self):
		self.isJumping = False
		self.isGoingDown = False

	def flipSpriteImage(self):
		return self.__spriteManager.flipSpriteImage()

	def jump(self):
		if(self.isJumping):
			if(self.isGoingDown):
				self.ActualPosition.Y += self.__speed.Y
				self.__speed.Y += 0.4
			else:
				if(self.__speed.Y <= 0):
					self.isGoingDown = True
				else:
					self.ActualPosition.Y -= self.__speed.Y
					self.__speed.Y -= 0.4

			if(self.thereIsTileBehind() and self.isGoingDown):
				self.endjumpCycle()
				self.stabilizeYPosition()
			else:
				if(self.ActualPosition.Y >= self.__screen.Y):
					self.endjumpCycle()
					self.__deathSound.play()
					self.setPotatoOnStartPosition()
					self.isStanding = True

	def jumpInitialize(self):
		if(not self.isJumping):
			self.__jumpSound.play()
			self.isStanding = False
			self.isJumping = True
			self.__speed.Y = 8

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
				self.ActualPosition.X -= self.__speed.X

		elif(Key.D in keysPressed):
			self.isStanding = False
			self.isGoingLeft = False
			if(not self.thereIsTileRight()):
				self.ActualPosition.X += self.__speed.X

		self.hasReachCheckpoint()
		self.updateImage()

		self.stayOnScreen()

	def moveOnYAxis(self):
		if((not self.isJumping) and (not self.thereIsTileBehind())):
			self.jumpInitialize()
			self.isGoingDown = True

	def newLevel(self, enviroment):
		self.__enviroment = enviroment
		self.setPotatoOnStartPosition()

	def hasReachCheckpoint(self):
		actualCord = Point(round(self.ActualPosition.X/30), round(self.ActualPosition.Y/30))
		self.reachCheckpoint = actualCord == self.__enviroment.getFinishCords()
		if(self.reachCheckpoint):
			self.__checkpointSound.play()

	def setPotatoOnStartPosition(self):
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0
		startCord = self.__enviroment.getStartCords()
		self.setActualPosition(startCord)

	def setActualPosition(self, point):
		self.ActualPosition = Point(point.X*30, point.Y*30)

	def stabilizeYPosition(self):
		self.ActualPosition.Y = round(self.ActualPosition.Y/30) * 30

	def stayOnScreen(self):
		if(self.ActualPosition.X < 0):
			self.ActualPosition.X = self.__screen.X
		elif(self.ActualPosition.X > self.__screen.X):
			self.ActualPosition.X = 0

	def thereIsTileBehind(self):
		behindPosition = Point(round((self.ActualPosition.X+10)/30), round(self.ActualPosition.Y/30) + 1)
		isTileBehind = self.__enviroment.isTile(behindPosition)
		self.__tracer.push("ActualPosition: {0}\n\rBehindPosition: {1}\n\risTileBehind: {2}",
			self.ActualPosition, behindPosition, isTileBehind)
		return isTileBehind

	def thereIsTileLeft(self):
		leftPosition = Point(round((self.ActualPosition.X-2)/30), round(self.ActualPosition.Y/30))
		isTileLeft = self.__enviroment.isTile(leftPosition)
		self.__tracer.push("ActualPosition: {0}\n\rLeftPosition: {1}\n\rIsTileLeft: {2}",
			self.ActualPosition, leftPosition, isTileLeft)
		return isTileLeft

	def thereIsTileRight(self):
		rightPosition = Point(round((self.ActualPosition.X/30)) + 1, round(self.ActualPosition.Y/30))
		isTileRight = self.__enviroment.isTile(rightPosition)
		self.__tracer.push("ActualPosition: {0}\n\rRightPosition: {1}\n\rIsTileRight: {2}",
			self.ActualPosition, rightPosition, isTileRight)
		return isTileRight

	def updateImage(self):
		imagePath = self.getImageToShow()

		self.updateSpriteImage(imagePath)

		if(not self.isGoingLeft):
			self.flipSpriteImage()

	def updateSpriteImage(self, imagePath):
		return self.__spriteManager.updateSpriteImage(imagePath)

	def updateSpritePosition(self):
		return self.__spriteManager.updateSprite(self.ActualPosition.X, self.ActualPosition.Y)
