#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class NullTracer(ITracer):
	
	def __init__(self):
		super(Tracer, self).__init__()
	
	def push(self, strToFormat, *args):
		pass

	def cls():
		pass