#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Block, resourcePath as rs


class Checkpoint(Block):

	def __init__(self, imageManager, spriteManager, position):
		Block.__init__(self, imageManager, spriteManager, rs.CHECKPOINT_IMAGE, position)
