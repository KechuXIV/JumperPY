#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from mock import Mock, MagicMock, call, NonCallableMock
from ...bin import Point
from ...bin.Motion import Motion

class test_Velocity(unittest.TestCase):

	def setUp(self):
		self.target = Motion()

	def test_GetVelocity(self):
		result = self.target.GetVelocity()
		
		self.assertEqual(result, Point(0,0))

