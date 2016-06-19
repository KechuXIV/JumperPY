#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import ISurfaceManager


class PygameSurfaceManager(ISurfaceManager):

	def __init__(self):
		self.surceface = None

	def createSurface(self, width, height):
		self.surceface = pygame.Surface([width, height], pygame.SRCALPHA, 32)

	def blitIntoSurface(self, image, width, height):
		self.surceface.blit(image, (width, height))

	def getSurface(self):
		return self.surceface
