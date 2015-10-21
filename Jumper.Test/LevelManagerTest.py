# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from LevelManager import *
from Point import *
from PygameImageManager import *
from PygameSurfaceManager import *
from PygameSpriteManager import *


class LevelManagerTest(unittest.TestCase):

	def setUp(self):
		imageManager = PygameImageManager()
		surfaceManager = PygameSurfaceManager()
		spriteManager = PygameSpriteManager()
		self.levelManager = LevelManager(imageManager, surfaceManager, spriteManager)

	def test_GetEnviroment(self):
		self.levelManager.GetRenderedLevel()
		enviroment = self.levelManager.GetEnviroment()

		self.assertIsNotNone(enviroment)
		self.assertEqual(enviroment.GetStartCords(), Point(1, 4))
		self.assertEqual(enviroment.GetFinishCords(), Point(18, 4))
		self.assertTrue(enviroment.IsTile(Point(0,4)))
		self.assertFalse(enviroment.IsTile(Point(2,4)))

	def test_GetEnviroment_ShouldRaiseExceptionIfNotRendered(self):
		with self.assertRaises(Exception) as cm:
			enviroment = self.levelManager.GetEnviroment()

		self.assertEqual(cm.exception.message, "Level not rendered")

	def test_GetLevel(self):
		expectedLevel = "leap_of_faith"

		actualLevel = self.levelManager.GetLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetLevelPath(self):
		expectedPath = "../Jumper.Core/Resources/levels/leap_of_faith.png"

		path = self.levelManager.GetLevelPath()

		self.assertEqual(path, expectedPath)

	def test_GetRenderedLevel(self):
		renderedLevel = self.levelManager.GetRenderedLevel()

		self.assertIsNotNone(renderedLevel)

	def test_GoToNextLevel(self):
		expectedLevel = "jumpering"

		actualLevel = self.levelManager.GoToNextLevel()

		self.assertEqual(actualLevel, expectedLevel)


if __name__ == '__main__':
	unittest.main()