# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from LevelManager import *
from PygameImageManager import *
from PygameSurfaceManager import *
from PygameSpriteManager import *


class LevelManagerTest(unittest.TestCase):

	def setUp(self):
		imageManager = PygameImageManager()
		surfaceManager = PygameSurfaceManager()
		spriteManager = PygameSpriteManager()
		self.levelManager = LevelManager(imageManager, surfaceManager, spriteManager)

	def test_GetLevel(self):
		expectedLevel = "leap_of_faith"

		actualLevel = self.levelManager.GetLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetRenderedLevel(self):
		renderedLevel = self.levelManager.GetRenderedLevel()

		self.assertIsNotNone(renderedLevel)

	def test_GoToNextLevel(self):
		expectedLevel = "jumpering"

		actualLevel = self.levelManager.GoToNextLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetLevelPath(self):
		expectedPath = "../Jumper.Core/Resources/levels/leap_of_faith.png"

		path = self.levelManager.GetLevelPath()

		self.assertEqual(path, expectedPath)

if __name__ == '__main__':
	unittest.main()