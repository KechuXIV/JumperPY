#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Point, Key, GameElement, Position, resourcePath as rs

class Potato(GameElement):

	def __init__(self, screenCords, spriteManager, enviroment, soundManager, tracer):
		GameElement.__init__(self, spriteManager, soundManager, enviroment, screenCords, Point(30, 30))
		self._tracer = tracer
		self._speed = Point(4, 6)
		self._enviroment = enviroment
		self._screenCords = screenCords

		self._images = [rs.POTATO_STANDING, rs.POTATO_WALKING, rs.POTATO_JUMPING]
		self._deathSound = self._getSound(rs.POTATO_DEATHSOUND)
		self._jumpSound = self._getSound(rs.POTATO_JUMPSOUND)
		self._checkpointSound = self._getSound(rs.POTATO_CHECKPOINTSOUND)

		self.setPotatoOnStartPosition()
		self._createSprite(self.ActualPosition)

	def getImageToShow(self):
		self.setActualImageIndex()
		return self._images[self.actualImageIndex]

	def getPosition(self, position):
		if(position == Position.BEHIND):
			return Point(round((self.ActualPosition.X+10)/30), round(self.ActualPosition.Y/30) + 1)
		elif(position == Position.LEFT):
			return Point(round((self.ActualPosition.X-2)/30), round(self.ActualPosition.Y/30))
		elif(position == Position.RIGHT):
			return Point(round((self.ActualPosition.X/30)) + 1, round(self.ActualPosition.Y/30))

	def getSprite(self):
		return self._getSprite()

	def endjumpCycle(self):
		self.isJumping = False
		self.isGoingDown = False

	def jump(self):
		if(not self.isJumping):
			return

		if(self.isGoingDown):
			self.ActualPosition.Y += self._speed.Y
			self._speed.Y += 0.4
		else:
			if(self._speed.Y <= 0):
				self.isGoingDown = True
			else:
				self.ActualPosition.Y -= self._speed.Y
				self._speed.Y -= 0.4

		if(self.thereIsTileBehind() and self.isGoingDown):
			self.endjumpCycle()
			self.stabilizeYPosition()
		else:
			if(self.ActualPosition.Y >= self._screenCords.Y):
				self.endjumpCycle()
				self._deathSound.play()
				self.setPotatoOnStartPosition()
				self.isStanding = True

	def jumpInitialize(self):
		if(not self.isJumping):
			self._jumpSound.play()
			self.isStanding = False
			self.isJumping = True
			self._speed.Y = 8

	def motion(self, keysPressed):
		self.isStanding = True
		if(Key.Space in keysPressed):
			self.jumpInitialize()

		self.moveOnXAxis(keysPressed)
		self.moveOnYAxis()

		self.jump()
		return self._updateSpritePosition(self.ActualPosition)

	def moveOnXAxis(self, keysPressed):
		if(Key.A in keysPressed):
			self.isStanding = False
			self.isGoingLeft = True
			if(not self.thereIsTileLeft()):
				self.ActualPosition.X -= self._speed.X
		elif(Key.D in keysPressed):
			self.isStanding = False
			self.isGoingLeft = False
			if(not self.thereIsTileRight()):
				self.ActualPosition.X += self._speed.X

		self.hasReachCheckpoint()
		self._updateImage(self.getImageToShow(), self.isGoingLeft)

		self.stayOnScreen()

	def moveOnYAxis(self):
		if((not self.isJumping) and (not self.thereIsTileBehind())):
			self.jumpInitialize()
			self.isGoingDown = True

	def newLevel(self, enviroment):
		self._enviroment = enviroment
		self.setPotatoOnStartPosition()

	def hasReachCheckpoint(self):
		actualCord = Point(round(self.ActualPosition.X/30), round(self.ActualPosition.Y/30))
		self.reachCheckpoint = actualCord == self._enviroment.getFinishCords()
		if(self.reachCheckpoint):
			self._checkpointSound.play()

	def setPotatoOnStartPosition(self):
		self.isJumping = False
		self.isGoingLeft = True
		self.isGoingDown = False
		self.isStanding = True
		self.reachCheckpoint = False
		self.actualImageIndex = 0
		startCord = self._enviroment.getStartCords()
		self.setActualPosition(startCord)

	def setActualImageIndex(self):
		if(self.isJumping | self.isGoingDown):
			self.actualImageIndex = 2
		elif(not self.isStanding):
			if(self.actualImageIndex > 1):
				self.actualImageIndex = 0
			else:
				self.actualImageIndex += 1
		else:
			self.actualImageIndex = 0

	def setActualPosition(self, point):
		self.ActualPosition = Point(point.X*30, point.Y*30)

	def stabilizeYPosition(self):
		self.ActualPosition.Y = round(self.ActualPosition.Y/30) * 30

	def stayOnScreen(self):
		if(self.ActualPosition.X < 0):
			self.ActualPosition.X = self._screenCords.X
		elif(self.ActualPosition.X > self._screenCords.X):
			self.ActualPosition.X = 0

	def thereIsTileBehind(self):
		behindPosition = self.getPosition(Position.BEHIND)
		isTileBehind = self._enviroment.isTile(behindPosition)
		return isTileBehind

	def thereIsTileLeft(self):
		leftPosition = self.getPosition(Position.LEFT)
		isTileLeft = self._enviroment.isTile(leftPosition)
		return isTileLeft

	def thereIsTileRight(self):
		rightPosition = self.getPosition(Position.RIGHT)
		isTileRight = self._enviroment.isTile(rightPosition)
		return isTileRight
