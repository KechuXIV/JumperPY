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
from mock import *
from ISoundManager import *
from ISpriteManager import *



class PotatoTest(unittest.TestCase):

    def setUp(self):
        screenWidth = 600
        screenHeight = 300
        tiles = [Point(0, 1),Point(1, 1), Point(2, 1), Point(19, 1), Point(0,4), Point(2,4), Point(0,5), Point(1,5), Point(2,5), Point(3,5)]
        #tiles = [Point(0, 1)]
        startCord = Point(0, 1)
        finishCord = Point(10, 1)

        self.__enviroment__ = Enviroment(startCord, finishCord, tiles)
        self.__screen__ = Point(screenWidth, screenHeight)
        self.__spriteManager__ = ISpriteManager()
        self.__soundManager__ = ISoundManager()

    def test_GetPotatoSprite(self):
        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.GetSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        sprite = target.GetSprite()

        pathDeathSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav')

        self.assertIsNotNone(spriteMock)
        self.assertEqual(sprite.Description, "Sprite Mockeado")
        calls = [call(pathDeathSound),call(pathJumpSound),call(pathCheckpointSound)]
        self.__soundManager__.GetSound.assert_has_calls(calls)

    def test_MovePotatoLeftInTheEdgeOfTheScreen(self):
        expectedPosition = Point(600,
            30)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        self.__spriteManager__.UpdateSpriteImage = MagicMock()

        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        keysPressed = []
        keysPressed.append(Key.A)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(0,0))
        sprite = target.Motion(keysPressed)

        pathDeathSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav')

        self.assertTrue(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.UpdateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotatoRightInTheEdgeOfTheScreen(self):
        expectedPosition = Point(585, 0)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()

        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        keysPressed = []
        keysPressed.append(Key.D)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(19,0))
        sprite = target.Motion(keysPressed)

        pathDeathSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav')

        self.assertFalse(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.UpdateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotato(self):
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(1,0))
        expectedPosition = target.ActualPosition

        target.Motion(keysPressed)

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)
        self.assertTrue(target.isStanding)

    def test_MovePotatoLeft(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,0))
        expectedPosition = Point(target.ActualPosition.X - target.__SPEED__.X,
            target.ActualPosition.Y)
        sprite = target.Motion(keysPressed)

        self.assertTrue(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.UpdateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotatoRight(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,0))
        expectedPosition = Point(target.ActualPosition.X + target.__SPEED__.X,
            target.ActualPosition.Y)
        sprite = target.Motion(keysPressed)

        self.assertFalse(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.UpdateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)


    def test_MovePotatoJump(self):
        
        keysPressed = []
        keysPressed.append(Key.Space)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(1,0))
        expectedPosition = Point(target.ActualPosition.X,
            target.ActualPosition.Y - target.__SPEED__.Y)
        target.Motion(keysPressed)

        self.assertFalse(target.isStanding)
        self.__spriteManager__.UpdateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_PotatoReachCheckpointFalse(self):
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(2,5))
        target.Motion(keysPressed)

        self.assertFalse(target.reachCheckpoint)

    def test_PotatoReachCheckpointTrue(self):
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(10,1))
        target.Motion(keysPressed)

        self.assertTrue(target.reachCheckpoint)

    def test_PotatoRebootScreenEnding(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.ActualPosition.X = target.__SCREEN__.X + 1
        target.ActualPosition.Y = 0

        sprite = target.Motion(keysPressed)
        
        self.__spriteManager__.UpdateSprite.assert_called_with(0, target.ActualPosition.Y)

    def test_PotatoRebootScreenStart(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.ActualPosition.X = 0
        target.ActualPosition.Y = 0

        sprite = target.Motion(keysPressed)

        self.__spriteManager__.UpdateSprite.assert_called_with(600, target.ActualPosition.Y)

    def test_PotatoDie(self):
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,20))
        target.isJumping = True
        target.isGoingDown = True
        
        target.Motion(keysPressed)

        self.assertEqual(Point(0,30), target.ActualPosition)

    def test_PotatoInitializeJumpWhenJumping(self):
        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.isJumping = True
        expectedStartJumpingCord = target.startJumpingCord

        target.JumpInitialize()

        self.assertTrue(target.isJumping)
        self.assertEqual(expectedStartJumpingCord, target.startJumpingCord)

    def test_PotatoInitializeJumpWhenNotJumping(self):
        expectedStartJumpingCord = 99

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.isJumping = False
        target.ActualPosition.Y = expectedStartJumpingCord

        target.JumpInitialize()

        self.assertTrue(target.isJumping)
        self.assertEqual(expectedStartJumpingCord, target.startJumpingCord)

    def test_PotatoJumpCycle(self):
        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,0))

        expectedPosition = Point(target.ActualPosition.X,
            target.ActualPosition.Y)

        target.JumpInitialize()
        for x in xrange(0,10):
            target.Jump()

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_SetPotatoActualPosition(self):
        x = 3
        y = 4

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(x, y))

        self.assertEqual(target.ActualPosition, Point(x*30,y*30))

    def test_ShouldNotMoveIfThereIsTileGoingRight(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,4))
        expectedPosition = Point(target.ActualPosition.X, target.ActualPosition.Y)

        target.Motion(keysPressed)

        self.assertEqual(target.ActualPosition, expectedPosition)
        
    def test_ShouldNotMoveIfThereIsTileGoingLeft(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(3,4))
        expectedPosition = Point(target.ActualPosition.X, target.ActualPosition.Y)

        target.Motion(keysPressed)

        self.assertEqual(target.ActualPosition, expectedPosition)

    def test_PotatoShouldDescendIfThereIsNotTileBehind(self):
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock()
        self.__spriteManager__.UpdateSprite = MagicMock()
        self.__spriteManager__.FlipSpriteImage = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,1))
        expectedPosition = Point(target.ActualPosition.X,
            target.ActualPosition.Y + target.__SPEED__.Y)

        target.Motion(keysPressed)

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition.Y, actualPosition.Y)
        self.assertEqual(expectedPosition, actualPosition)
        self.assertFalse(target.isStanding)
        self.assertTrue(target.isGoingDown)
        self.assertTrue(target.isJumping)

    def test_ThereIsTileBehindTrue(self):
        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,0))
        
        thereIsTileBehind = target.ThereIsTileBehind()

        self.assertTrue(thereIsTileBehind)

    def test_ThereIsTileBehindFalse(self):
        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.SetActualPosition(Point(1,1))
        
        thereIsTileBehind = target.ThereIsTileBehind()

        self.assertFalse(thereIsTileBehind)

if __name__ == '__main__':
    unittest.main()