#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Block, resourcePath as rs


class Tile(Block):

	def __init__(self, imageManager, spriteManager, position):
		Block.__init__(self, imageManager, spriteManager, rs.TILE_IMAGE, position)
