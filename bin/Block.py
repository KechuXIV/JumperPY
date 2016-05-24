#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Block(object):
    __slot__ = ['Width', 'Height', 'Image']
    
    def __init__(self, imageManager, path):
        self.Width = 30
        self.Height = 30
        self.Image = imageManager.createImage(self.Width, self.Height, path)