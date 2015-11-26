# -*- coding: utf-8 -*-
import os


class Tile():

	def __init__(self, imageManager):
		self.Width = 30
		self.Height = 30
		path = os.path.join('..', 'Jumper.Core','Resources', 'tile.png')
		self.Image = imageManager.CreateImage(self.Width, self.Height, path)