#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from mock import Mock, MagicMock, call, NonCallableMock
from ....bin import Point
from ....bin.Motion import Motion
from ....bin.Motion.Decorator import MotionRightDecorator

class test_MotionRightDecorator(unittest.TestCase):

	def setUp(self):
		self.motion = Mock(spec=Motion)
		self.target = MotionRightDecorator(self.motion)

	def test_GetVelocity(self):
		self.motion.GetVelocity.return_value = Point(0,0)

		result = self.target.GetVelocity()
		
		self.assertEqual(result, Point(4,0))

