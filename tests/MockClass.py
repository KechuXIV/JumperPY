#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getColor(r, g, b):
	if((0,0,0) == (r,g,b)):
		return "Black"
	elif((255, 0, 0) == (r,g,b)):
		return "Red"
	elif((76, 255, 0) == (r,g,b)):
		return "Green"
	else:
		return "Color"
		
		
class MockPixelArray(object):
	
	def __getitem__(self, k):
		return 5