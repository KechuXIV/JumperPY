# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from Point import *


class PointTest(unittest.TestCase):

	def setUp(self):
		self.Point = Point()

	def test_DevuelveString(self):
		stringEsperado = "(5;3)"
		self.Point.X = 5
		self.Point.Y = 3

		stringActual = str(self.Point)

		self.assertEqual(stringEsperado, stringActual) 

if __name__ == '__main__':
	unittest.main()