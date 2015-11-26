# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from LevelManager import *
from mock import MagicMock
from Point import *
from IImageManager import *
from ISurfaceManager import *
from ISpriteManager import *


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
		expectedPath = "../Jumper.Core/Resources/levels/leap_of_faith.png"
		self.__imageManager__.CreateImage = MagicMock()
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		path = target.GetLevelPath()

		self.assertEqual(path, expectedPath)

	def test_GetRenderedLevel(self):
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
		
		target = LevelManager(self.__imageManager__, self.__surfaceManager__, self.__spriteManager__)
		renderedLevel = target.GetRenderedLevel()

		self.assertIsNotNone(renderedLevel)

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