#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import ISoundManager


class PygameSoundManager(ISoundManager):

	def __init__(self):
		pygame.init()

	def getSound(self, soundPath):
		return pygame.mixer.Sound(soundPath)
