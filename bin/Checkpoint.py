#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Checkpoint():

	def __init__(self, imageManager):
		Block.__init__(self, imageManager, os.path.join('..', 'bin','Resources', 'checkpoint.png'))