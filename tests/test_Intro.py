#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from ..bin import Intro, ISpriteManager, Point
from mock import Mock, MagicMock, call, NonCallableMock


class test_Intro(unittest.TestCase):

	def setUp(self):
		self.screen = Point(600, 300)
		self.spriteManager = Mock(spec=ISpriteManager)

		self.target = Intro(self.screen, self.spriteManager)

		self.spriteManagerExpected = []

	def tearDown(self):
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpected)

	def test_GetSprite(self):
		spriteMock = NonCallableMock()
		self.spriteManager.getSprite.return_value = spriteMock

		sprite = self.target.getSprite()

		self.spriteManagerExpected.append(call.createSpriteFromImagePath(0, 0, 600, 300,
			os.path.join('JumperPY', 'bin','Resources', 'menu.png')))
		self.spriteManagerExpected.append(call.getSprite())

		self.assertIsNotNone(spriteMock)
		self.assertEqual(sprite, spriteMock)
