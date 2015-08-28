# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from Potato import *
from Point import *
from Key import *
from PygameSpriteManager import *


class PotatoTest(unittest.TestCase):

    def setUp(self):
        self.spriteManager = PygameSpriteManager()
        self.potato = Potato(self.spriteManager)

    def test_MovePotato(self):
        expectedPosition = self.potato.ActualPosition
        keysPressed = []

        self.potato.Motion(keysPressed)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)

    def test_MovePotatoLeft(self):
        expectedPosition = Point(self.potato.ActualPosition.X - self.potato.__SPEED__.X,
            self.potato.ActualPosition.Y)
        keysPressed = []
        keysPressed.append(Key.A)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)

    def test_MovePotatoRight(self):
        expectedPosition = Point(self.potato.ActualPosition.X + self.potato.__SPEED__.X,
            self.potato.ActualPosition.Y)
        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)

    def test_MovePotatoJump(self):
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y - self.potato.__SPEED__.Y)
        keysPressed = []
        keysPressed.append(Key.Space)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)

    def test_PotatoJumpCycle(self):
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y)

        self.potato.JumpInitialize()
        for x in xrange(0,10):
            self.potato.Jump()

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_PotatoInitializeJumpWhenJumping(self):
        self.potato.isJumping = True
        expectedStartJumpingCord = self.potato.startJumpingCord

        self.potato.JumpInitialize()

        self.assertTrue(self.potato.isJumping)
        self.assertEqual(expectedStartJumpingCord, self.potato.startJumpingCord)

    def test_PotatoInitializeJumpWhenNotJumping(self):
        self.potato.isJumping = False
        expectedStartJumpingCord = 99
        self.potato.ActualPosition.Y = expectedStartJumpingCord

        self.potato.JumpInitialize()

        self.assertTrue(self.potato.isJumping)
        self.assertEqual(expectedStartJumpingCord, self.potato.startJumpingCord)

    def test_GetPotatoSprite(self):
        expectedPosition = self.potato.ActualPosition

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