# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from ImageManager import *
from Tile import *


class TileTest(unittest.TestCase):

	def setUp(self):
		imageManager = ImageManager() 
		self.tile = Tile(imageManager)

	def test_GetTileHeightAndWidth(self):
		expectedHeight = 30
		expectedWidth = 30

		height = self.tile.Height
		witdh = self.tile.Width

		self.assertEqual(height, expectedHeight)
		self.assertEqual(witdh, expectedWidth)

	def test_GetTileImage(self):
		image = self.tile.Image

		self.assertIsNotNone(image)

if __name__ == '__main__':
	unittest.main()