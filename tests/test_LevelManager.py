#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'ui'))
sys.path.append(lib_path)

from LevelManager import *
from mock import MagicMock, Mock, call, NonCallableMock, NonCallableMagicMock
from Point import *
from IImageManager import *
from ISurfaceManager import *
from ISpriteManager import *


def getColor(r, g, b):
	if((0,0,0) == (r,g,b)):
		return "Black"
	elif((255, 0, 0) == (r,g,b)):
		return "Red"
	elif((76, 255, 0) == (r,g,b)):
		return "Green"
	else:
		return "Color"
		
class mockPixelArray(object):
	
	def __getitem__(self, k):
		return 5

class test_LevelManager(unittest.TestCase):

	def setUp(self):
		self.imageManager = Mock(spec=IImageManager)
		self.surfaceManager = Mock(spec=ISurfaceManager)
		self.spriteManager = Mock(spec=ISpriteManager)
		attrs = {'Width.return_value': 30, 'Height.return_value': 30}
		self.tile = MagicMock()
		self.checkpoint = MagicMock()
		
		self.target = LevelManager(self.imageManager, 
			self.surfaceManager, self.spriteManager,
			self.tile, self.checkpoint)
			
		self.imageManagerExpects = []
		self.surfaceManagerExpects = []
		self.spriteManagerExpects = []
		
	def tearDown(self):
		self.assertEqual(self.imageManager.mock_calls, self.imageManagerExpects)
		self.assertEqual(self.surfaceManager.mock_calls, self.surfaceManagerExpects)
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpects)

	def test_getEnviroment(self):
		mockEnviroment = MagicMock()
		mockSurface = MagicMock()
		
		self.imageManager.createImage.return_value = mockSurface
 		
		self.target.enviroment = mockEnviroment
		enviroment = self.target.getEnviroment()

		self.assertIsNotNone(enviroment)
		self.assertEqual(enviroment, mockEnviroment)

	def test_GetEnviroment_ShouldRaiseExceptionIfNotRendered(self):
		with self.assertRaises(Exception) as cm:
			enviroment = self.target.getEnviroment()

		self.assertEqual(cm.exception.message, "Level not rendered")

	def test_GetLevel(self):
		expectedLevel = "leap_of_faith"
		
		actualLevel = self.target.getLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetLevelPath(self):
		expectedPath = "../bin/Resources/levels/leap_of_faith.png"
		
		path = self.target.getLevelPath()

		self.assertEqual(path, expectedPath)
		
	def test_GetRenderedLevel(self):
		self.tile.Width = 30
		self.tile.Height = 30
		
		pixelArray = mockPixelArray()
		#pixelArray.__getitem__ = Mock(return_value = 5)
		sourceface = Mock()
		
		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = 20
		self.imageManager.getImageHeight.return_value = 12
		self.imageManager.getImageColor.side_effect = getColor
		self.surfaceManager.getSurface.return_value = sourceface
		
		self.imageManagerExpects.append(call.loadImage(os.path.join('..', 'bin','Resources','levels', 'leap_of_faith.png')))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())
		self.imageManagerExpects.append(call.getImageColor(0, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(255, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(76, 255, 0))
		
		for i in range(0,240):
			self.imageManagerExpects.append(call.getPixelArrayItemColor(5))
			
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())	
		self.surfaceManagerExpects.append(call.createSurface(30*20, 30*12))
		self.surfaceManagerExpects.append(call.getSurface())
		self.spriteManagerExpects.append(call.createSpriteFromSurface(0, 0, 600, 360, sourceface))
		self.spriteManagerExpects.append(call.getSprite())
		 
		renderedLevel = self.target.getRenderedLevel()
		
		self.assertIsNotNone(renderedLevel)

	def test_GoToNextLevel(self):
		self.tile.Width = 30
		self.tile.Height = 30
		
		pixelArray = Mock()
		pixelArray.__getitem__ = Mock(return_value=5)
		sourceface = Mock()
		
		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = 20
		self.imageManager.getImageHeight.return_value = 12
		self.imageManager.getImageColor.side_effect = getColor
		self.surfaceManager.getSurface.return_value = sourceface
		
		self.surfaceManagerExpects.append(call.createSurface(30*20, 30*12))
		self.surfaceManagerExpects.append(call.getSurface())
		self.spriteManagerExpects.append(call.updateSpriteFromSurface(0, 0, 600, 360, sourceface))
		self.spriteManagerExpects.append(call.getSprite())
		
		renderedLevel = self.target.goToNextLevel()
		
		# No se como hacer para generar el call de pixel array
		self.imageManagerExpects.extend(self.imageManager.mock_calls)
		
		self.assertIsNotNone(renderedLevel)

if __name__ == "__main__":
    unittest.main()
    
class C(object):
    def __getitem__(self, k):
        return k