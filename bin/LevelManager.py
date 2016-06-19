#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Enviroment, ResourcePath as rs
from .Point import Point


class LevelManager(object):

	def __init__(self, imageManager, surcefaceManager,
		spriteManager, tile, checkpoint):
		self.__imageManager = imageManager
		self.__spriteManager = spriteManager
		self.__surfaceManager = surcefaceManager
		self.__actualLevel = 0
		self.__sprite = None
		self.enviroment = None

		self.__levels = self.getLevels()
		self.__tile = tile
		self.__checkpoint = checkpoint

	def createSpriteFromSurface(self):
		sourceface = self.__surfaceManager.getSurface()
		width = self.__imageManager.getImageWidth()
		height = self.__imageManager.getImageHeight()
		self.__spriteManager.createSpriteFromSurface(0, 0,
			width*self.__tile.Width, height*self.__tile.Height, sourceface)

	def getEnviroment(self):
		print("Cosa{0}".format(self.enviroment is None))
		if self.enviroment is None:
			raise Exception("Level not rendered")
		return self.enviroment

	def getLevel(self):
		return self.__levels[self.__actualLevel]

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

		return self.__sprite

	def getSprite(self):
		self.__sprite = self.__spriteManager.getSprite()

	def goToNextLevel(self):
		if(self.__actualLevel >= (len(self.__levels)-1)):
			self.__actualLevel = 0	
		self.__actualLevel += 1

		self.loadAndRenderLevel()
		self.updateSpriteFromSurface()
		self.getSprite()
		
		return self.__sprite 

	def loadAndRenderLevel(self):
		level = self.getLevel()

		self.__imageManager.loadImage(level)
		
		width = self.__imageManager.getImageWidth()
		height = self.__imageManager.getImageHeight()

		pixelArray = self.__imageManager.getPixelArray()

		black = self.__imageManager.getImageColor(0, 0, 0)
		red = self.__imageManager.getImageColor(255, 0, 0)
		green = self.__imageManager.getImageColor(76, 255, 0)

		self.__surfaceManager.createSurface(width*self.__tile.Width,
			height*self.__tile.Height)

		startCord = None
		finishCord = None
		tilesCords = []

		for x in xrange(0,width):
			for y in xrange(0,height):
				color = self.__imageManager.getPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						self.__surfaceManager.blitIntoSurface(self.__tile.Image,
							x*self.__tile.Width, y*self.__tile.Height)
						tilesCords.append(Point(x, y))
				elif color == red:
					if(x != 20): 
						startCord = Point(x, y)
				elif color == green:
					if(x != 20): 
						self.__surfaceManager.blitIntoSurface(self.__checkpoint.Image,
							x*self.__tile.Width, y*self.__tile.Height)
						finishCord = Point(x, y)

		self.enviroment = Enviroment(startCord, finishCord, tilesCords)

	def updateSpriteFromSurface(self):
		sourceface = self.__surfaceManager.getSurface()
		width = self.__imageManager.getImageWidth()
		height = self.__imageManager.getImageHeight()
		self.__spriteManager.updateSpriteFromSurface(0, 0, width*self.__tile.Width,
			height*self.__tile.Height, sourceface)