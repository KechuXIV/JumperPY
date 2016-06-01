#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from ITracer import ITracer


class NullTracer(ITracer):
	
	def __init__(self):
		super(NullTracer, self).__init__()
	
	def push(self, strToFormat, *args):
		pass

	def cls():
		pass