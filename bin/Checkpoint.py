#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import Block


class Checkpoint(Block):

	def __init__(self, imageManager):
		Block.__init__(self, imageManager, os.path.join('JumperPY','bin','Resources', 'checkpoint.png'))