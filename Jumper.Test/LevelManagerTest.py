# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from LevelManager import *


class LevelManagerTest(unittest.TestCase):

	def setUp(self):
		self.levelManager = LevelManager()

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

if __name__ == '__main__':
	unittest.main()