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
from mock import *
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

class test_LevelManager(unittest.TestCase):

	def setUp(self):
		self.__imageManager__ = IImageManager()
		self.__surfaceManager__ = ISurfaceManager()
		self.__spriteManager__ = ISpriteManager()

	def test_GetEnviroment(self):
		mockEnviroment = MagicMock()
		mockEnviroment.Description = "enviroment mockeado"
		mockSurface = MagicMock()
		mockSurface.Description = "surface mock"
		self.__imageManager__.createImage = MagicMock(return_value=mockSurface)
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		target.enviroment = mockEnviroment
		enviroment = target.getEnviroment()

		self.assertIsNotNone(enviroment)
		self.assertEqual(enviroment.Description, "enviroment mockeado")

	def test_GetEnviroment_ShouldRaiseExceptionIfNotRendered(self):
		with self.assertRaises(Exception) as cm:
			self.__imageManager__.createImage = MagicMock()
			target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
			enviroment = target.getEnviroment()

		self.assertEqual(cm.exception.message, "Level not rendered")

	def test_GetLevel(self):
		expectedLevel = "leap_of_faith"
		self.__imageManager__.createImage = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		actualLevel = target.getLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetLevelPath(self):
		expectedPath = "../bin/Resources/levels/leap_of_faith.png"
		self.__imageManager__.createImage = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		path = target.getLevelPath()

		self.assertEqual(path, expectedPath)
		
	def test_GetRenderedLevel(self):
		self.__imageManager__.createImage = MagicMock()
		self.__imageManager__.loadImage = MagicMock()
		self.__imageManager__.getImageWidth = MagicMock(return_value=20)
		self.__imageManager__.getImageHeight = MagicMock(return_value=12)
		self.__imageManager__.getPixelArray = MagicMock()
		self.__imageManager__.getImageColor = Mock(None, side_effect=getColor)
		self.__imageManager__.getPixelArrayItemColor = MagicMock()
		self.__surfaceManager__.createSurface = MagicMock()
		self.__surfaceManager__.getSurface = MagicMock()
		self.__spriteManager__.createSpriteFromSurface = MagicMock()
		self.__spriteManager__.getSprite = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		renderedLevel = target.getRenderedLevel()

		self.assertIsNotNone(renderedLevel)
		self.__imageManager__.loadImage.assert_called_with(os.path.join('..', 'bin','Resources','levels', 'leap_of_faith.png'))
		self.__imageManager__.getImageWidth.assert_called_with()
		self.__imageManager__.getImageHeight.assert_called_with()
		self.__imageManager__.getPixelArray.assert_called_with()
		calls = [call(0, 0, 0),call(255, 0, 0),call(76, 255, 0)]
		self.__imageManager__.getImageColor.assert_has_calls(calls, any_order=False)
		self.__surfaceManager__.createSurface.assert_called_with(20*30, 12*30)

	def test_GoToNextLevel(self):
		self.__imageManager__.createImage = MagicMock()
		self.__imageManager__.loadImage = MagicMock()
		self.__imageManager__.getImageWidth = MagicMock()
		self.__imageManager__.getImageHeight = MagicMock()
		self.__imageManager__.getPixelArray = MagicMock()
		self.__imageManager__.getImageColor = MagicMock()
		self.__imageManager__.getPixelArrayItemColor = MagicMock()
		self.__surfaceManager__.createSurface = MagicMock()
		self.__surfaceManager__.getSurface = MagicMock()
		self.__spriteManager__.createSpriteFromSurface = MagicMock()
		self.__spriteManager__.getSprite = MagicMock()
		self.__spriteManager__.updateSpriteFromSurface = MagicMock()
	
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		actualLevel = target.goToNextLevel()

		self.assertIsNotNone(actualLevel)

if __name__ == "__main__":
    unittest.main()