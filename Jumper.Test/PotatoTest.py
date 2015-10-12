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
        screenWidth = 600
        screenHeight = 300
        screen = Point(screenWidth, screenHeight)
        self.spriteManager = PygameSpriteManager()
        self.potato = Potato(screen, self.spriteManager)

    def test_MovePotato(self):
        expectedPosition = self.potato.ActualPosition
        keysPressed = []

        self.potato.Motion(keysPressed)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)
        self.assertTrue(self.potato.isStanding)

    def test_MovePotatoLeft(self):
        expectedPosition = Point(self.potato.ActualPosition.X - self.potato.__SPEED__.X,
            self.potato.ActualPosition.Y)
        keysPressed = []
        keysPressed.append(Key.A)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertTrue(self.potato.isGoingLeft)
        self.assertFalse(self.potato.isStanding)

    def test_MovePotatoRight(self):
        expectedPosition = Point(self.potato.ActualPosition.X + self.potato.__SPEED__.X,
            self.potato.ActualPosition.Y)
        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertFalse(self.potato.isGoingLeft)
        self.assertFalse(self.potato.isStanding)

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

    def test_PotatoCantGoOutsideFromScreenEnding(self):
        self.potato.ActualPosition.X = self.potato.__SCREEN__.X

        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, self.potato.__SCREEN__.X - self.potato.__WIDTH__)

    def test_PotatoCantGoOutsideFromScreenStart(self):
        self.potato.ActualPosition.X = 0

        keysPressed = []
        keysPressed.append(Key.A)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, 0)

    def test_GetPotatoSprite(self):
        expectedPosition = self.potato.ActualPosition

        sprite = self.potato.GetSprite()

        self.assertIsNotNone(sprite)
        self.assertIsNotNone(sprite.image)
        self.assertIsNotNone(sprite.rect)
        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertEqual(30, sprite.rect.height)
        self.assertEqual(30, sprite.rect.width)

if __name__ == '__main__':
    unittest.main()