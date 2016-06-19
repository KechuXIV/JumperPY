#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from ..bin import Point


class test_Point(unittest.TestCase):

	def setUp(self):
		self.target = Point()

	def tearDown(self):
		pass

	def test_ToString(self):
		expectedString = "(5;3)"
		self.target.X = 5
		self.target.Y = 3

		string = str(self.target)

		self.assertEqual(string, expectedString)

	def test_Equal(self):
		expectedPoint = Point(1,3)
		self.target.X = 1
		self.target.Y = 3

		self.assertEqual(self.target, expectedPoint)

	def test_NotEqual(self):
		notPoint = Point(4,5)
		self.target.X = 4
		self.target.Y = 5

		self.assertNotEqual(self.target, notPoint)
