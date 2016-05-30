#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from ISoundManager import *

class PygameSoundManager(ISoundManager):

	def __init__(self):
		pygame.init()

	def getSound(self, soundPath):
		return pygame.mixer.Sound(soundPath)