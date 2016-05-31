#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ITracer(object):

	def __init__(self):
		super(ITracer, self).__init__()

	def push(self, strToFormat, *args):
		raise NotImplementedError("Should have implemented this")

	def cls():
		raise NotImplementedError("Should have implemented this")
