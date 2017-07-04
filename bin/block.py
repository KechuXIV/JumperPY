#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Block(object):

	def __init__(self, imageManager, spriteManager, path, position):
		self.Position = position
		self.Width = 30
		self.Height = 30
		self.Image = imageManager.createImage(self.Width, self.Height, path)
		self.Sprite = spriteManager.createSprite(self.Position.X, 
			self.Position.Y, self.Width, self.Height, self.Image)
