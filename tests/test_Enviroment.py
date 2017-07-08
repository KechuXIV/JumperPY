#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest
import uuid

from ..bin import Enviroment, Point


class test_Enviroment(unittest.TestCase):

	def setUp(self):
		self._startCords = Point(0, 0)
		self._tiles = [str(uuid.uuid4()),str(uuid.uuid4())]
		self._checkpoint = str(uuid.uuid4())
		self.target = Enviroment(self._startCords, self._checkpoint, self._tiles)

	def tearDown(self):
		pass

	def test_getCheckpoints(self):
		result = self.target.getCheckpoints()
		self.assertEqual(result, self._checkpoint)

	def test_getStartCords(self):
		result = self.target.getStartCords()
		self.assertEqual(result, self._startCords)

	def test_getTiles(self):
		result = self.target.getTiles()
		self.assertEqual(self._tiles, result)
