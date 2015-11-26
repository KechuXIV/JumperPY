# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from mock import MagicMock
from PygameImageManager import *
from Tile import *


class TileTest(unittest.TestCase):

	def setUp(self):
		self.__imageManager__ = PygameImageManager()

	def test_GetTileHeightAndWidth(self):
		expectedHeight = 30
		expectedWidth = 30

		self.__imageManager__.CreateImage = MagicMock()
		target = Tile(self.__imageManager__)

		height = target.Height
		witdh = target.Width

		self.__imageManager__.CreateImage.assert_called_with(expectedWidth, expectedHeight, os.path.join('..', 'Jumper.Core','Resources', 'tile.png'))
		self.assertEqual(height, expectedHeight)
		self.assertEqual(witdh, expectedWidth)

	def test_GetTileImage(self):
		self.__imageManager__.CreateImage = MagicMock()
		target = Tile(self.__imageManager__)

		image = target.Image

		self.assertIsNotNone(image)

if __name__ == '__main__':
	unittest.main()