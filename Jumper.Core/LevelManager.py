# -*- coding: utf-8 -*-
import os
import pygame

from Tile import *


class LevelManager():



	def __init__(self):
		self.__actualLevel__ = 15

		self.levels = self.GetLevels() 

	def GetLevel(self):
		return self.levels[self.__actualLevel__]

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
		tile = Tile()

		levelPath = os.path.join('..', 'Jumper.Core','Resources','levels', self.GetLevel() + '.png')
		surfaceLevelPath = pygame.image.load(levelPath)
		pixelArray = pygame.PixelArray(surfaceLevelPath)
		width = surfaceLevelPath.get_width()
		height = surfaceLevelPath.get_height()

		black = pygame.Color(surfaceLevelPath.map_rgb((0, 0, 0)))
		red = pygame.Color(surfaceLevelPath.map_rgb((255, 0, 0)))
		green = pygame.Color(surfaceLevelPath.map_rgb((76, 255, 0)))

		surceface = pygame.Surface([width*32,height*32], pygame.SRCALPHA, 32)

		for x in xrange(0,width):
			for y in xrange(0,height):
 				color = pygame.Color(pixelArray[x, y])
				if color == black:
					surceface.blit(tile.Image,(x*30,y*30))
				elif color == red:
					pass
				elif color == green:
					pass

		sprite = pygame.sprite.Sprite()
		sprite.image = surceface
		sprite.rect = pygame.Rect((0, 0), (width*30, height*30))

		return sprite

	def GoToNextLevel(self):
		self.__actualLevel__ += 1

		return self.levels[self.__actualLevel__]