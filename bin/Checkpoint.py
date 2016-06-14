#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Block, ResourcePath as rs


class Checkpoint(Block):

	def __init__(self, imageManager):
		Block.__init__(self, imageManager, rs.CHECKPOINT_IMAGE)
