#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

lib_path = os.path.abspath(os.path.join('bin'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from Enviroment import *
from Point import *

class test_Enviroment(unittest.TestCase):

	def setUp(self):
		startCords = Point(0, 0)
		finishCords = Point(2, 3)
		tiles = [Point(1, 2),Point(4, 5)]
		self.target = Enviroment(startCords, finishCords, tiles)

	def test_GetStartCords(self):
		expectedCords = Point(0, 0)

		startCords = self.target.getStartCords()

		self.assertEqual(startCords, expectedCords)

	def test_GetFinishCords(self):
		expectedCords = Point(2, 3)

		finishCords = self.target.getFinishCords()

		self.assertEqual(finishCords, expectedCords)

	def test_isTileShouldTrue(self):
		point = Point(1, 2)

		isTile = self.target.isTile(point)

		self.assertTrue(isTile)

	def test_isTileShouldFalse(self):
		point = Point(0, 0)

		isTile = self.target.isTile(point)

		self.assertFalse(isTile)
		
if __name__ == "__main__":
    unittest.main()