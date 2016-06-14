#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Enviroment
from .Point import Point


class LevelManager(object):

	def __init__(self, imageManager, surcefaceManager,
		spriteManager, tile, checkpoint):
		self.imageManager = imageManager
		self.spriteManager = spriteManager
		self.surfaceManager = surcefaceManager
		self.__actualLevel = 0
		self.__sprite = None
		self.enviroment = None

		self.__levels = self.getLevels()
		self.__tile = tile
		self.__checkpoint = checkpoint

	def createSpriteFromSurface(self):
		sourceface = self.surfaceManager.getSurface()
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()
		self.spriteManager.createSpriteFromSurface(0, 0, width*self.__tile.Width, height*self.__tile.Height, sourceface)

	def getEnviroment(self):
		print("Cosa{0}".format(self.enviroment is None))
		if self.enviroment is None:
			raise Exception("Level not rendered")
		return self.enviroment

	def getLevel(self):
		return self.__levels[self.__actualLevel]

	def getLevelPath(self):
		return os.path.join('JumperPY', 'bin','Resources','levels', self.getLevel() + '.png')

	def getLevels(self):
		levels = []
		levels.append("leap_of_faith")
		levels.append("jumpering")
		levels.append("think_fast")
		levels.append("not_so_hard_maze")
		levels.append("one_jump")
		levels.append("ruins")
		levels.append("jumper")
		levels.append("nl10")
		levels.append("free_runner")
		levels.append("unknown")
		levels.append("nl9")
		levels.append("woah")
		levels.append("roof_climber")
		levels.append("zigzag")
		levels.append("nl7")
		levels.append("jump")
		levels.append("luck")
		levels.append("tower")
		levels.append("cheap_level")
		levels.append("just_an_other_level")
		levels.append("perhaps")
		levels.append("trial")
		levels.append("nl1")
		levels.append("nl6")
		levels.append("nl4")
		levels.append("spam")
		levels.append("nl3")
		levels.append("nl8")
		levels.append("bad_level")
		levels.append("frustration")
		levels.append("nl2")
		levels.append("pure_luck")
		levels.append("wild_guess")
		levels.append("nl5")
		levels.append("fly")

		return levels

	def getRenderedLevel(self):
		self.loadAndRenderLevel()
		self.createSpriteFromSurface()
		self.getSprite()

		return self.__sprite

	def getSprite(self):
		self.__sprite = self.spriteManager.getSprite()

	def goToNextLevel(self):
		if(self.__actualLevel >= (len(self.__levels)-1)):
			self.__actualLevel = 0	
		self.__actualLevel += 1

		self.loadAndRenderLevel()
		self.updateSpriteFromSurface()
		self.getSprite()
		
		return self.__sprite 

	def loadAndRenderLevel(self):
		levelPath = self.getLevelPath()

		self.imageManager.loadImage(levelPath)
		
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()

		pixelArray = self.imageManager.getPixelArray()

		black = self.imageManager.getImageColor(0, 0, 0)
		red = self.imageManager.getImageColor(255, 0, 0)
		green = self.imageManager.getImageColor(76, 255, 0)

		self.surfaceManager.createSurface(width*self.__tile.Width, height*self.__tile.Height)

		startCord = None
		finishCord = None
		tilesCords = []

		for x in xrange(0,width):
			for y in xrange(0,height):
 				color = self.imageManager.getPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						self.surfaceManager.blitIntoSurface(self.__tile.Image, x*self.__tile.Width, y*self.__tile.Height)
						tilesCords.append(Point(x, y))
				elif color == red:
					if(x != 20): 
						startCord = Point(x, y)
				elif color == green:
					if(x != 20): 
						self.surfaceManager.blitIntoSurface(self.__checkpoint.Image, x*self.__tile.Width, y*self.__tile.Height)
						finishCord = Point(x, y)

		self.enviroment = Enviroment(startCord, finishCord, tilesCords)

	def updateSpriteFromSurface(self):
		sourceface = self.surfaceManager.getSurface()
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()
		self.spriteManager.updateSpriteFromSurface(0, 0, width*self.__tile.Width, height*self.__tile.Height, sourceface)