#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from Point import Point
from Key import Key

class Intro(object):
    
    def __init__(self, screen, spriteManager):
        self.__screen = screen
        self.__spriteManager = spriteManager
        self.image = 'menu.png'
        
        self.__createSprite()

    def __createSprite(self):
        imagePath = self.__getImagePath(self.image)

        self.__spriteManager.createSprite(0, 0,
			self.__screen.X, self.__screen.Y, imagePath)

    def __getImagePath(self, image):
		return os.path.join('..', 'bin','Resources', image)
        
    def getSprite(self):
        return self.__spriteManager.getSprite()
        
