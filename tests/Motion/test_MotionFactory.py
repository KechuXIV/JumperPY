#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from mock import Mock, MagicMock, call, NonCallableMock
from ...bin import Point, Key
from ...bin.Motion import MotionFactory
from ...bin.Motion.Decorator import MotionGravityDecorator 
from ...bin.Motion.Decorator import MotionJumpDecorator 
from ...bin.Motion.Decorator import MotionLeftDecorator 
from ...bin.Motion.Decorator import MotionRightDecorator 

class test_MotionFactory(unittest.TestCase):

	def setUp(self):
		self.target = MotionFactory()

	def test_CreateEmpty(self):
		keysPressed = []
		result = self.target.Create(keysPressed)
		
		self.assertIsInstance(result, MotionGravityDecorator)

	def test_Create_A(self):
		keysPressed = [Key.A]
		result = self.target.Create(keysPressed)
		
		self.assertIsInstance(result, MotionLeftDecorator)

	def test_Create_D(self):
		keysPressed = [Key.D]
		result = self.target.Create(keysPressed)
		
		self.assertIsInstance(result, MotionRightDecorator)

	def test_Create_Space(self):
		keysPressed = [Key.Space]
		result = self.target.Create(keysPressed)
		
		self.assertIsInstance(result, MotionJumpDecorator)
