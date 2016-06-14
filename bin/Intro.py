#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ResourcePath as rs

from . import Point, Key

class Intro(object):
    
    def __init__(self, screen, spriteManager):
        self.__screen = screen
        self.__spriteManager = spriteManager
        self.__imagePath = rs.INTRO_IMAGE
        self.gameStart = False
        
        self.__createSprite()

    def __createSprite(self):
        self.__spriteManager.createSprite(0, 0,
			self.__screen.X, self.__screen.Y, self.__imagePath)
        
    def getSprite(self):
        return self.__spriteManager.getSprite()
        
