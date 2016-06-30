#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Block, resourcePath as rs


class Tile(Block):

	def __init__(self, imageManager):
		Block.__init__(self, imageManager, rs.TILE_IMAGE)
