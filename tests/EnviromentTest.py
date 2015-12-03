#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from Enviroment import *
from Point import *

class EnviromentTest(unittest.TestCase):

	def setUp(self):
		startCords = Point(0, 0)
		finishCords = Point(2, 3)
		tiles = [Point(1, 2),Point(4, 5)]
		self.enviroment = Enviroment(startCords, finishCords, tiles)

	def test_GetStartCords(self):
		expectedCords = Point(0, 0)

		startCords = self.enviroment.GetStartCords()

		self.assertEqual(startCords, expectedCords)

	def test_GetFinishCords(self):
		expectedCords = Point(2, 3)

		finishCords = self.enviroment.GetFinishCords()

		self.assertEqual(finishCords, expectedCords)

	def test_isTileShouldTrue(self):
		point = Point(1, 2)

		isTile = self.enviroment.IsTile(point)

		self.assertTrue(isTile)

	def test_isTileShouldFalse(self):
		point = Point(0, 0)

		isTile = self.enviroment.IsTile(point)

		self.assertFalse(isTile)

if __name__ == '__main__':
	unittest.main()