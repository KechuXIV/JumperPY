# -*- coding: utf-8 -*-
import os
import pygame

from Tile import *


class LevelManager():

	def __init__(self, imageManager, surcefaceManager, spriteManager):
		self.__actualLevel__ = 0
		self.__sprite__ = None
		self.imageManager = imageManager
		self.surfaceManager = surcefaceManager
		self.spriteManager = spriteManager

		self.levels = self.GetLevels()
		self.tile = Tile(imageManager) 

	def GetLevel(self):
		return self.levels[self.__actualLevel__]

	def GetLevelPath(self):
		return os.path.join('..', 'Jumper.Core','Resources','levels', self.GetLevel() + '.png')

	def GetLevels(self):
		levels = ["leap_of_faith"]
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

	def GetRenderedLevel(self):
		levelPath = self.GetLevelPath()

		self.imageManager.LoadImage(levelPath)
		
		width = self.imageManager.GetImageWidth()
		height = self.imageManager.GetImageHeight()

		pixelArray = self.imageManager.GetPixelArray()

		black = self.imageManager.GetImageColor(0, 0, 0)
		red = self.imageManager.GetImageColor(255, 0, 0)
		green = self.imageManager.GetImageColor(76, 255, 0)

		self.surfaceManager.CreateSurface(width*self.tile.Width, height*self.tile.Height)

		for x in xrange(0,width):
			for y in xrange(0,height):
 				color = self.imageManager.GetPixelArrayItemColor(pixelArray[x, y])
				if color == black:
					self.surfaceManager.BlitIntoSurface(self.tile.Image, x*self.tile.Width, y*self.tile.Height)
				elif color == red:
					pass
				elif color == green:
					pass

		sourceface = self.surfaceManager.GetSurface()

		self.spriteManager.CreateSpriteFromSurface(0, 0, width*self.tile.Width, height*self.tile.Height, sourceface)

		self.__sprite__ = self.spriteManager.GetSprite()

		return self.__sprite__

	def GoToNextLevel(self):
		self.__actualLevel__ += 1

		return self.levels[self.__actualLevel__]