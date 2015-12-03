#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from ISurfaceManager import *


class PygameSurfaceManager(ISurfaceManager):

	def __init__(self):
		self.surceface = None

	def CreateSurface(self, width, height):
		self.surceface = pygame.Surface([width, height], pygame.SRCALPHA, 32)

	def BlitIntoSurface(self, image, width, height):
		self.surceface.blit(image, (width, height))

	def GetSurface(self):
		return self.surceface
	