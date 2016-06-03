#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from . import ITracer

class Tracer(ITracer):
	
	def __init__(self):
		super(Tracer, self).__init__()
	
	def push(self, strToFormat, *args):
		print(strToFormat.format(*list(args)))

	def cls(self):
		os.system('clear')
