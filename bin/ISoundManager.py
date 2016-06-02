#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ISoundManager(object):

	def getSound(self, soundPath):
		raise NotImplementedError("Should have implemented this")