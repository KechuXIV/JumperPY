# -*- coding: utf-8 -*-
import os
import pygame

class Tile():

	def __init__(self):
		self.Path = os.path.join('..', 'Jumper.Core','Resources', 'tile.png')
		self.Width = 30
		self.Height = 30
		self.Image = pygame.transform.scale(pygame.image.load(self.Path), (self.Width, self.Height))