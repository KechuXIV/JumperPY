#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from Point import *


class PointTest(unittest.TestCase):

	def setUp(self):
		self.Point = Point()

	def test_ToString(self):
		expectedString = "(5;3)"
		self.Point.X = 5
		self.Point.Y = 3

		string = str(self.Point)

		self.assertEqual(string, expectedString)

	def test_Equal(self):
		expectedPoint = Point(1,3)
		self.Point.X = 1
		self.Point.Y = 3

		self.assertEqual(self.Point, expectedPoint)

	def test_NotEqual(self):
		notPoint = Point(4,5)
		self.Point.X = 4
		self.Point.Y = 5

		self.assertNotEqual(self.Point, notPoint)

if __name__ == '__main__':
	unittest.main()