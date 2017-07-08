#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Checkpoint, Tile, Point, resourcePath as rs, Enviroment


class LevelManager(object):

	def __init__(self, imageManager, surcefaceManager, spriteManager):
		self._imageManager = imageManager
		self._spriteManager = spriteManager
		self._surfaceManager = surcefaceManager
		self._actualLevel = 0
		self._sprite = None
		self._enviroment = None

		self._colorBlack = self._imageManager.getColor(255, 0, 0, 0)
		self._colorRed = self._imageManager.getColor(255, 0, 0, 255)
		self._colorGreen = self._imageManager.getColor(255, 0, 255, 76)

		self._levels = self.getLevels()

	def getLevel(self):
		return self._levels[self._actualLevel]

	def getLevels(self):
		levels = []
		levels.append(rs.LEVEL_LEAP_OF_FAITH)
		levels.append(rs.LEVEL_JUMPERING)
		levels.append(rs.LEVEL_THINK_FAST)
		levels.append(rs.LEVEL_NOT_SO_HARD_MAZE)
		levels.append(rs.LEVEL_ONE_JUMP)
		levels.append(rs.LEVEL_RUINS)
		levels.append(rs.LEVEL_JUMPER)
		levels.append(rs.LEVEL_NL10)
		levels.append(rs.LEVEL_FREE_RUNNER)
		levels.append(rs.LEVEL_UNKNOWN)
		levels.append(rs.LEVEL_NL9)
		levels.append(rs.LEVEL_ROOF_CLIMBER)
		levels.append(rs.LEVEL_ZIGZAG)
		levels.append(rs.LEVEL_NL7)
		levels.append(rs.LEVEL_JUMP)
		levels.append(rs.LEVEL_LUCK)
		levels.append(rs.LEVEL_TOWER)
		levels.append(rs.LEVEL_CHEAP_LEVEL)
		levels.append(rs.LEVEL_JUST_AN_OTHER_LEVEL)
		levels.append(rs.LEVEL_PERHAPS)
		levels.append(rs.LEVEL_TRIAL)
		levels.append(rs.LEVEL_NL1)
		levels.append(rs.LEVEL_NL6)
		levels.append(rs.LEVEL_NL4)
		levels.append(rs.LEVEL_SPAM)
		levels.append(rs.LEVEL_NL3)
		levels.append(rs.LEVEL_NL8)
		levels.append(rs.LEVEL_BAD_LEVEL)
		levels.append(rs.LEVEL_FRUSTRATION)
		levels.append(rs.LEVEL_NL2)
		levels.append(rs.LEVEL_PURE_LUCK)
		levels.append(rs.LEVEL_WILD_GUESS)
		levels.append(rs.LEVEL_NL5)
		levels.append(rs.LEVEL_FLY)

		return levels

	def goToNextLevel(self):
		if(self._actualLevel >= (len(self._levels)-1)):
			self._actualLevel = 0
		self._actualLevel += 1

		return self.getEnviroment()

	def getEnviroment(self):
		level = self.getLevel()

		self._imageManager.loadImage(level)

		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()

		pixelArray = self._imageManager.getPixelArray()

		return self.getTilesFromPixelArray(width, height, pixelArray)

	def getTilesFromPixelArray(self, width, height, pixelArray):
		tiles = []
		checkpoints = []
		startCord = None
		for x in xrange(0,width):
			for y in xrange(0,height):
				block = self.getBlockByColorInPixelArray(pixelArray, x, y)
				if(type(block) == Checkpoint):
					checkpoints.append(block)
				elif(type(block) == Tile):
					tiles.append(block)
				elif(type(block) == Point):
					startCord = block

		return Enviroment(startCord, checkpoints, tiles)

	def getBlockByColorInPixelArray(self, pixelArray, x, y):
		color = self._imageManager.getPixelArrayItemColor(pixelArray[x, y])
		block = None
		if color == self._colorBlack:
			block = Tile(self._imageManager, self._spriteManager, Point(x*30, y*30))
		elif color == self._colorRed:
			block = Point(x, y)
		elif color == self._colorGreen:
			block = Checkpoint(self._imageManager, self._spriteManager, Point(x*30, y*30))

		return block

	def updateSpriteFromSurface(self):
		sourceface = self._surfaceManager.getSurface()
		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()
		self._spriteManager.updateSpriteFromSurface(0, 0, width*self._tile.Width,
			height*self._tile.Height, sourceface)
