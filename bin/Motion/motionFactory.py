#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import Motion
from .Decorator import MotionGravityDecorator
from .Decorator import MotionJumpDecorator
from .Decorator import MotionLeftDecorator
from .Decorator import MotionRightDecorator
from .. import Key

class MotionFactory(object):

	def __init__(self):
		pass

	def Create(self, keysPressed):
		motion = MotionGravityDecorator(Motion())

		if Key.A in keysPressed:
			motion = MotionLeftDecorator(motion)
		if Key.D in keysPressed:
			motion = MotionRightDecorator(motion)
		if Key.Space in keysPressed:
			motion = MotionJumpDecorator(motion)

		return motion