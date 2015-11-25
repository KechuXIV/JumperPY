# -*- coding: utf-8 -*-
import unittest
import sys
import os

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'Jumper.UI'))
sys.path.append(lib_path)

from Enviroment import *
from Key import *
from Point import *
from Potato import *
from PygameSoundManager import *
from PygameSpriteManager import *



class PotatoTest(unittest.TestCase):

    def setUp(self):
        screenWidth = 600
        screenHeight = 300
        screen = Point(screenWidth, screenHeight)
        self.spriteManager = PygameSpriteManager()
        soundManager = PygameSoundManager()

        tiles = [Point(0, 1),Point(1, 1), Point(2, 1), Point(19, 1)]
        startCord = Point(0, 1)
        finishCord = Point(10, 1)

        enviroment = Enviroment(startCord, finishCord, tiles)
        self.potato = Potato(screen, self.spriteManager, enviroment, soundManager)

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

    def test_MovePotatoLeftStayingOnScreen(self):
        self.potato.SetActualPosition(Point(0,0))
        expectedPosition = Point(600,
            30)

        keysPressed = []
        keysPressed.append(Key.A)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertTrue(self.potato.isGoingLeft)
        self.assertFalse(self.potato.isStanding)

    def test_MovePotatoRightStayingOnScreen(self):
        self.potato.SetActualPosition(Point(19,0))
        expectedPosition = Point(585,
            self.potato.ActualPosition.Y)

        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)
        self.assertFalse(self.potato.isGoingLeft)
        self.assertFalse(self.potato.isStanding)

    def test_MovePotato(self):
        self.potato.SetActualPosition(Point(1,0))
        expectedPosition = self.potato.ActualPosition
        keysPressed = []

        self.potato.Motion(keysPressed)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)
        self.assertTrue(self.potato.isStanding)

    def test_MovePotatoLeft(self):
        self.potato.SetActualPosition(Point(1,0))
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
        self.potato.SetActualPosition(Point(1,0))
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
        self.potato.SetActualPosition(Point(1,0))
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y - self.potato.__SPEED__.Y)
        keysPressed = []
        keysPressed.append(Key.Space)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(expectedPosition.X, sprite.rect.x)
        self.assertEqual(expectedPosition.Y, sprite.rect.y)

    def test_PotatoReachCheckpointFalse(self):
        self.potato.SetActualPosition(Point(2, 5))
        keysPressed = []

        self.potato.Motion(keysPressed)

        self.assertFalse(self.potato.reachCheckpoint)

    def test_PotatoReachCheckpointTrue(self):
        self.potato.SetActualPosition(Point(10, 1))
        keysPressed = []
        self.potato.Motion(keysPressed)

        self.assertTrue(self.potato.reachCheckpoint)

    def test_PotatoCantGoOutsideFromScreenEnding(self):
        self.potato.ActualPosition.X = self.potato.__SCREEN__.X

        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, 0)

    def test_PotatoCantGoOutsideFromScreenStart(self):
        self.potato.ActualPosition.X = 570

        keysPressed = []
        keysPressed.append(Key.A)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, 555)

    def test_PotatoDie(self):
        self.potato.SetActualPosition(Point(1,20))
        self.potato.isJumping = True
        self.potato.isGoingDown = True
        keysPressed = []
        
        self.potato.Motion(keysPressed)

        self.assertEqual(Point(0,30), self.potato.ActualPosition)

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

    def test_PotatoJumpCycle(self):
        self.potato.SetActualPosition(Point(1,0))
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y)

        self.potato.JumpInitialize()
        for x in xrange(0,10):
            self.potato.Jump()

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_SetPotatoActualPosition(self):
        x = 3
        y = 4
        self.potato.SetActualPosition(Point(x, y))

        self.assertEqual(self.potato.ActualPosition, Point(x*30,y*30))

    def test_PotatoShouldDescendIfThereIsNotTileBehind(self):
        self.potato.SetActualPosition(Point(1,1))
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y + self.potato.__SPEED__.Y)
        keysPressed = []

        self.potato.Motion(keysPressed)

        actualPosition = self.potato.ActualPosition

        self.assertEqual(expectedPosition.Y, actualPosition.Y)
        self.assertEqual(expectedPosition, actualPosition)
        self.assertFalse(self.potato.isStanding)
        self.assertTrue(self.potato.isGoingDown)
        self.assertTrue(self.potato.isJumping)

    def test_ThereIsTileBehindTrue(self):
        self.potato.SetActualPosition(Point(1,0))
        
        thereIsTileBehind = self.potato.ThereIsTileBehind()

        self.assertTrue(thereIsTileBehind)

    def test_ThereIsTileBehindFalse(self):
        self.potato.SetActualPosition(Point(1,1))
        
        thereIsTileBehind = self.potato.ThereIsTileBehind()

        self.assertFalse(thereIsTileBehind)

if __name__ == '__main__':
    unittest.main()