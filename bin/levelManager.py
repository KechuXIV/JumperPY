#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Tile, Point, resourcePath as rs, Enviroment


class LevelManager(object):

	def __init__(self, imageManager, surcefaceManager,
		spriteManager, tile, checkpoint):
		self._imageManager = imageManager
		self._spriteManager = spriteManager
		self._surfaceManager = surcefaceManager
		self._actualLevel = 0
		self._sprite = None
		self._enviroment = None

		self._levels = self.getLevels()
		self._tile = tile
		self._checkpoint = checkpoint

	def createSpriteFromSurface(self):
		sourceface = self._surfaceManager.getSurface()
		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()
		self._spriteManager.createSpriteFromSurface(0, 0,
			width*self._tile.Width, height*self._tile.Height, sourceface)

	def getEnviroment(self):
		if self._enviroment is None:
			raise Exception("Level not rendered")
		return self._enviroment

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

	def getRenderedLevel(self):
		self.loadAndRenderLevel()
		self.createSpriteFromSurface()
		self.getSprite()

		return self._sprite

	def getSprite(self):
		self._sprite = self._spriteManager.getSprite()

	def goToNextLevel(self):
		if(self._actualLevel >= (len(self._levels)-1)):
			self._actualLevel = 0
		self._actualLevel += 1

		self.loadAndRenderLevel()
		self.updateSpriteFromSurface()
		self.getSprite()
		
		return self._sprite 

	def loadAndRenderLevel(self):
		level = self.getLevel()

		self._imageManager.loadImage(level)
		
		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()

		pixelArray = self._imageManager.getPixelArray()

		black = self._imageManager.getImageColor(0, 0, 0)
		red = self._imageManager.getImageColor(255, 0, 0)
		green = self._imageManager.getImageColor(76, 255, 0)

		self._surfaceManager.createSurface(width*self._tile.Width,
			height*self._tile.Height)

		startCord = None
		finishCord = None
		tilesCords = []

		for x in xrange(0,width):
			for y in xrange(0,height):
				color = self._imageManager.getPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						self._surfaceManager.blitIntoSurface(self._tile.Image,
							x*self._tile.Width, y*self._tile.Height)
						tilesCords.append(Point(x, y))
				elif color == red:
					if(x != 20): 
						startCord = Point(x, y)
				elif color == green:
					if(x != 20): 
						self._surfaceManager.blitIntoSurface(self._checkpoint.Image,
							x*self._tile.Width, y*self._tile.Height)
						finishCord = Point(x, y)

		self._enviroment = Enviroment(startCord, finishCord, tilesCords)

	def getLevelSprites(self):
		sprites = []

		level = self.getLevel()

		self._imageManager.loadImage(level)
		
		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()

		pixelArray = self._imageManager.getPixelArray()

		black = self._imageManager.getImageColor(0, 0, 0)
		red = self._imageManager.getImageColor(255, 0, 0)
		green = self._imageManager.getImageColor(76, 255, 0)

		tiles = []
		for x in xrange(0,width):
			for y in xrange(0,height):
				color = self._imageManager.getPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						tiles.append(Tile(self._imageManager, self._spriteManager, Point(x*30, y*30)))
				elif color == red:
					if(x != 20): 
						pass#startCord
				elif color == green:
					if(x != 20): 
						pass#FinishCord

		return tiles

	def updateSpriteFromSurface(self):
		sourceface = self._surfaceManager.getSurface()
		width = self._imageManager.getImageWidth()
		height = self._imageManager.getImageHeight()
		self._spriteManager.updateSpriteFromSurface(0, 0, width*self._tile.Width,
			height*self._tile.Height, sourceface)
