# -*- coding: utf-8 -*-
import unittest
import sys
import os

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

class LevelManagerTest(unittest.TestCase):

	def setUp(self):
		self.__imageManager__ = IImageManager()
		self.__surfaceManager__ = ISurfaceManager()
		self.__spriteManager__ = ISpriteManager()

	def test_GetEnviroment(self):
		mockEnviroment = MagicMock()
		mockEnviroment.Description = "enviroment mockeado"
		mockSurface = MagicMock()
		mockSurface.Description = "surface mock"
		self.__imageManager__.CreateImage = MagicMock(return_value=mockSurface)
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		target.enviroment = mockEnviroment
		enviroment = target.GetEnviroment()

		self.assertIsNotNone(enviroment)
		self.assertEqual(enviroment.Description, "enviroment mockeado")

	def test_GetEnviroment_ShouldRaiseExceptionIfNotRendered(self):
		with self.assertRaises(Exception) as cm:
			self.__imageManager__.CreateImage = MagicMock()
			target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
			enviroment = target.GetEnviroment()

		self.assertEqual(cm.exception.message, "Level not rendered")

	def test_GetLevel(self):
		expectedLevel = "leap_of_faith"
		self.__imageManager__.CreateImage = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		actualLevel = target.GetLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetLevelPath(self):
		expectedPath = "../bin/Resources/levels/leap_of_faith.png"
		self.__imageManager__.CreateImage = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		path = target.GetLevelPath()

		self.assertEqual(path, expectedPath)
		
	def test_GetRenderedLevel(self):
		self.__imageManager__.CreateImage = MagicMock()
		self.__imageManager__.LoadImage = MagicMock()
		self.__imageManager__.GetImageWidth = MagicMock(return_value=20)
		self.__imageManager__.GetImageHeight = MagicMock(return_value=12)
		self.__imageManager__.GetPixelArray = MagicMock()
		self.__imageManager__.GetImageColor = Mock(None, side_effect=getColor)
		self.__imageManager__.GetPixelArrayItemColor = MagicMock()
		self.__surfaceManager__.CreateSurface = MagicMock()
		self.__surfaceManager__.GetSurface = MagicMock()
		self.__spriteManager__.CreateSpriteFromSurface = MagicMock()
		self.__spriteManager__.GetSprite = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		renderedLevel = target.GetRenderedLevel()

		self.assertIsNotNone(renderedLevel)
		self.__imageManager__.LoadImage.assert_called_with(os.path.join('..', 'bin','Resources','levels', 'leap_of_faith.png'))
		self.__imageManager__.GetImageWidth.assert_called_with()
		self.__imageManager__.GetImageHeight.assert_called_with()
		self.__imageManager__.GetPixelArray.assert_called_with()
		calls = [call(0, 0, 0),call(255, 0, 0),call(76, 255, 0)]
		self.__imageManager__.GetImageColor.assert_has_calls(calls, any_order=False)
		self.__surfaceManager__.CreateSurface.assert_called_with(20*30, 12*30)

	def test_GoToNextLevel(self):
		self.__imageManager__.CreateImage = MagicMock()
		self.__imageManager__.LoadImage = MagicMock()
		self.__imageManager__.GetImageWidth = MagicMock()
		self.__imageManager__.GetImageHeight = MagicMock()
		self.__imageManager__.GetPixelArray = MagicMock()
		self.__imageManager__.GetImageColor = MagicMock()
		self.__imageManager__.GetPixelArrayItemColor = MagicMock()
		self.__surfaceManager__.CreateSurface = MagicMock()
		self.__surfaceManager__.GetSurface = MagicMock()
		self.__spriteManager__.CreateSpriteFromSurface = MagicMock()
		self.__spriteManager__.GetSprite = MagicMock()
		self.__spriteManager__.UpdateSpriteFromSurface = MagicMock()
	
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		actualLevel = target.GoToNextLevel()

		self.assertIsNotNone(actualLevel)


if __name__ == '__main__':
	unittest.main()
	
