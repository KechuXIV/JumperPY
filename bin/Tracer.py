#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Tracer(ITracer):
	
	def __init__(self):
		super(Tracer, self).__init__()
	
	def push(self, strToFormat, *args):
		cls()
		print(strToFormat.format(*list(args)))

	def cls():
		os.system('cls' if os.name=='nt' else 'clear')