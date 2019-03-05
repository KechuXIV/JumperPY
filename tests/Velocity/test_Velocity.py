import sys
import os
import unittest

from ...bin import Point
from ...bin.Velocity import Velocity


class test_Velocity(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_IsStanding(self):
		velocity = Velocity(Point(0, 0))

		self.assertTrue(velocity.isStanding())

	def test_IsNotStanding(self):
		velocity = Velocity(Point(1, 0))
		
		self.assertFalse(velocity.isStanding())
		
	def test_IsGoingLeft(self):
		velocity = Velocity(Point(-1, 0))
		
		self.assertTrue(velocity.isGoingLeft())

	def test_IsGoingRight(self):
		velocity = Velocity(Point(1, 0))
		
		self.assertFalse(velocity.isGoingLeft())

	def test_IsGoingUp(self):
		velocity = Velocity(Point(5, 8))
		
		self.assertTrue(velocity.isGoingUp())

	def test_IsGoingDown(self):
		velocity = Velocity(Point(9, -4))
		
		self.assertFalse(velocity.isGoingUp())

