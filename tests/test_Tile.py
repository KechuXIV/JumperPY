#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

#sys.path.append(os.path.abspath(os.path.join('bin')))
#sys.path.append(os.path.abspath(os.path.join('..','bin')))

from ..bin import IImageManager, Tile
from mock import MagicMock, Mock, call


class test_Tile(unittest.TestCase):

	def setUp(self):
		self.imageManager = Mock(spec=IImageManager)
		
		self.target = Tile(self.imageManager)
		
		self.imageManagerExpects = []
		
	def tearDown(self):
		self.assertEqual(self.imageManager.mock_calls, self.imageManagerExpects)

	def test_GetTileHeightAndWidth(self):
		expectedHeight = 30
		expectedWidth = 30

		self.imageManagerExpects.append(call.createImage(30, 30, os.path.join('..', 'bin','Resources', 'tile.png')))

		height = self.target.Height
		witdh = self.target.Width

		self.assertEqual(height, expectedHeight)
		self.assertEqual(witdh, expectedWidth)

	def test_GetTileImage(self):
		self.imageManagerExpects.append(call.createImage(30, 30, os.path.join('..', 'bin','Resources', 'tile.png')))

		image = self.target.Image
		
		self.assertIsNotNone(image)

if __name__ == "__main__":
    unittest.main()