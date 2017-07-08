#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest
import uuid
import random

from ..bin import IImageManager, ISpriteManager, Tile, Point, resourcePath as rs
from mock import MagicMock, Mock, call


class test_Tile(unittest.TestCase):

	def setUp(self):
		self.imageManager = Mock(spec=IImageManager)
		self.spriteManager = Mock(spec=ISpriteManager)
		self.position = Point(int(random.random()*500),int(random.random()*500))
		self.sprite = str(uuid.uuid4())
		self.image = str(uuid.uuid4())
		self.width = 30
		self.height = 30

		self.imageManager.createImage.return_value = self.image
		self.spriteManager.createNewSprite.return_value = self.sprite

		self.target = Tile(self.imageManager, self.spriteManager, self.position)

		self.imageManagerExpects= [call.createImage(self.width, self.height, rs.TILE_IMAGE)]
		self.spriteManagerExpects = [call.createNewSprite(self.position.X, 
			self.position.Y, self.width, self.height, self.image)]


	def tearDown(self):
		self.assertEqual(self.imageManager.mock_calls, self.imageManagerExpects)
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpects)

	def test_GetTileHeightAndWidth(self):
		height = self.target.Height
		witdh = self.target.Width

		self.assertEqual(height, self.height)
		self.assertEqual(witdh, self.width)

	def test_GetImage(self):
		image = self.target.Image

		self.assertEqual(image, self.image)

	def test_GetSprite(self):
		sprite = self.target.Sprite

		self.assertEqual(sprite, self.sprite)
