# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from Tile import *


class TileTest(unittest.TestCase):

	def setUp(self):
		self.tile = Tile()

	def test_GetTilePath(self):
		expectedPath = "../Jumper.Core/Resources/tile.png"
		path = self.tile.Path
		self.assertEqual(path, expectedPath)

	def test_GetTileHeightAndWidth(self):
		expectedHeight = 32
		expectedWidth = 32

		height = self.tile.Height
		witdh = self.tile.Width

		self.assertEqual(height, expectedHeight)
		self.assertEqual(witdh, expectedWidth)

	def test_GetTileImage(self):
		image = self.tile.Image

		self.assertIsNotNone(image)

if __name__ == '__main__':
	unittest.main()