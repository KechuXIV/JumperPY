# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from Potato import *
from Point import *
from Key import *


class PotatoTest(unittest.TestCase):

    def setUp(self):
        self.potato = Potato()

    def test_MovePotato(self):
        expectedPosition = self.potato.ActualPosition
        key = None

        self.potato.Motion(key)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)

    def test_MovePotatoLeft(self):
        expectedPosition = Point(self.potato.ActualPosition.X - self.potato.__velocidadEnX__,
            self.potato.ActualPosition.Y)
        key = Key.A

        self.potato.Motion(key)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_MovePotatoRight(self):
        expectedPosition = Point(self.potato.ActualPosition.X + self.potato.__velocidadEnX__,
            self.potato.ActualPosition.Y)
        key = Key.D

        self.potato.Motion(key)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_GetPotatoSprite(self):
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y)

        sprite = self.potato.GetSprite()

        self.assertTrue(sprite is not None)
        self.assertTrue(sprite.image is not None)
        self.assertTrue(sprite.rect is not None)
        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertEqual(30, sprite.rect.width)
        self.assertEqual(30, sprite.rect.height)
        

if __name__ == '__main__':
    unittest.main()