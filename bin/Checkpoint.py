#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Block import Block


class Checkpoint(Block):

	def __init__(self, imageManager):
		Block.__init__(self, imageManager, os.path.join('..', 'bin','Resources', 'checkpoint.png'))