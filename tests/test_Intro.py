#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join('bin')))
sys.path.append(os.path.abspath(os.path.join('..','bin')))

from Intro import Intro
from ISpriteManager import ISpriteManager
from mock import Mock, MagicMock, call, NonCallableMock
from Point import Point

class test_Intro(unittest.TestCase):
    
    def setUp(self):
        self.screen = Point(600, 300)
        self.spriteManager = Mock(spec=ISpriteManager)
        
        self.target = Intro(self.screen, self.spriteManager)
		
        self.spriteManagerExpected = []
		
    def tearDown(self):
        self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpected)
    
    def test_GetSprite(self):
        spriteMock = NonCallableMock()
        
        self.spriteManager.getSprite.return_value = spriteMock
        
        sprite = self.target.getSprite()

        self.spriteManagerExpected.append(call.createSprite(0, 0, 600, 300, '../bin/Resources/menu.png'))
        self.spriteManagerExpected.append(call.getSprite())
    
        self.assertIsNotNone(spriteMock)
        self.assertEqual(sprite, spriteMock)
    
if __name__ == "__main__":
    unittest.main()
