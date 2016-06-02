#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from Enviroment import Enviroment


class LevelManager(object):

	def __init__(self, imageManager, surcefaceManager,
		spriteManager, tile, checkpoint):
		self.__actualLevel__ = 0
		self.__sprite__ = None
		self.imageManager = imageManager
		self.enviroment = None
		self.surfaceManager = surcefaceManager
		self.spriteManager = spriteManager

		self.levels = self.getLevels()
		self.tile = tile
		self.checkpoint = checkpoint

	def createSpriteFromSurface(self):
		sourceface = self.surfaceManager.getSurface()
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()
		self.spriteManager.createSpriteFromSurface(0, 0, width*self.tile.Width, height*self.tile.Height, sourceface)

	def getEnviroment(self):
		if self.enviroment is None:
			raise Exception("Level not rendered")
		return self.enviroment

	def getLevel(self):
		return self.levels[self.__actualLevel__]

	def getLevelPath(self):
		return os.path.join('..', 'bin','Resources','levels', self.getLevel() + '.png')

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

		return self.__sprite__

	def getSprite(self):
		self.__sprite__ = self.spriteManager.getSprite()

	def goToNextLevel(self):
		if(self.__actualLevel__ >= (len(self.levels)-1)):
			self.__actualLevel__ = 0	
		self.__actualLevel__ += 1

		self.loadAndRenderLevel()
		self.updateSpriteFromSurface()
		self.getSprite()
		
		return self.__sprite__ 

	def loadAndRenderLevel(self):
		levelPath = self.getLevelPath()

		self.imageManager.loadImage(levelPath)
		
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()

		pixelArray = self.imageManager.getPixelArray()

		black = self.imageManager.getImageColor(0, 0, 0)
		red = self.imageManager.getImageColor(255, 0, 0)
		green = self.imageManager.getImageColor(76, 255, 0)

		self.surfaceManager.createSurface(width*self.tile.Width, height*self.tile.Height)

		startCord = None
		finishCord = None
		tilesCords = []

		for x in xrange(0,width):
			for y in xrange(0,height):
 				color = self.imageManager.getPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					if(x != 20):
						self.surfaceManager.blitIntoSurface(self.tile.Image, x*self.tile.Width, y*self.tile.Height)
						tilesCords.append(Point(x, y))
				elif color == red:
					if(x != 20): 
						startCord = Point(x, y)
				elif color == green:
					if(x != 20): 
						self.surfaceManager.blitIntoSurface(self.checkpoint.Image, x*self.tile.Width, y*self.tile.Height)
						finishCord = Point(x, y)

		self.enviroment = Enviroment(startCord, finishCord, tilesCords)

	def updateSpriteFromSurface(self):
		sourceface = self.surfaceManager.getSurface()
		width = self.imageManager.getImageWidth()
		height = self.imageManager.getImageHeight()
		self.spriteManager.updateSpriteFromSurface(0, 0, width*self.tile.Width, height*self.tile.Height, sourceface)