#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

lib_path = os.path.abspath(os.path.join('bin'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join('..', 'ui'))
sys.path.append(lib_path)

from Enviroment import *
from Key import *
from Point import *
from Potato import *
from mock import *
from ISoundManager import *
from ISpriteManager import *


class test_Potato(unittest.TestCase):

    def setUp(self):
        screenWidth = 600
        screenHeight = 300
        
        tiles = [Point(0, 1), Point(0,4), Point(0,5), Point(1, 1), Point(1,5), Point(2, 1), Point(2,4), Point(2,5),Point(3,5), Point(4,5), Point(19, 1)]
        # Boceto de Tiles:
        #   [0][1][2][3][4][5][6][7][8][9][0][1][2][3][4][5][6][7][8][9]
        #[0] 
        #[1][x][x][x]                                                [x]
        #[2]
        #[3]
        #[4][x]   [x]
        #[5][x][x][x][x][x]
        #[6]
        #[7]
        #[8]
        #[9]
        #----------------------------------------------------------------
        startCord = Point(0, 1)
        finishCord = Point(10, 1)

        self.__enviroment__ = Enviroment(startCord, finishCord, tiles)
        self.__screen__ = Point(screenWidth, screenHeight)
        self.__spriteManager__ = ISpriteManager()
        self.__soundManager__ = ISoundManager()

    def test_GetPotatoSprite(self):
        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.getSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        sprite = target.getSprite()

        pathDeathSound = os.path.join('..', 'bin','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'bin','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'bin','Resources', 'sounds', 'checkpoint.wav')

        self.assertIsNotNone(spriteMock)
        self.assertEqual(sprite.Description, "Sprite Mockeado")
        calls = [call(pathDeathSound),call(pathJumpSound),call(pathCheckpointSound)]
        self.__soundManager__.getSound.assert_has_calls(calls)

    def test_MovePotatoLeftInTheEdgeOfTheScreen(self):
        expectedPosition = Point(600, 8)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        self.__spriteManager__.updateSpriteImage = MagicMock()

        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.updateSprite = MagicMock(return_value=spriteMock)

        keysPressed = []
        keysPressed.append(Key.A)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.setActualPosition(Point(0,0))
        sprite = target.motion(keysPressed)

        pathDeathSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav')

        self.assertTrue(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.updateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotatoRightInTheEdgeOfTheScreen(self):
        expectedPosition = Point(572, 0)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()

        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.updateSprite = MagicMock(return_value=spriteMock)

        keysPressed = []
        keysPressed.append(Key.D)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.setActualPosition(Point(19,0))
        sprite = target.motion(keysPressed)

        pathDeathSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'Jumper.Core','Resources', 'sounds', 'checkpoint.wav')

        self.assertFalse(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.updateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotato(self):
        keysPressed = []

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.setActualPosition(Point(1,0))
        expectedPosition = target.ActualPosition

        target.motion(keysPressed)

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)
        self.assertTrue(target.isStanding)

    def test_MovePotatoLeft(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.updateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,0))
        target.isGoingLeft = False
        expectedPosition = Point(target.ActualPosition.X - target.__SPEED__.X,
            target.ActualPosition.Y)
        sprite = target.motion(keysPressed)

        self.assertTrue(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.updateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotatoRight(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.updateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,0))
        expectedPosition = Point(target.ActualPosition.X + target.__SPEED__.X,
            target.ActualPosition.Y)
        sprite = target.motion(keysPressed)

        self.assertFalse(target.isGoingLeft)
        self.assertFalse(target.isStanding)
        self.__spriteManager__.updateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)

    def test_MovePotatoJump(self):
        keysPressed = []
        keysPressed.append(Key.Space)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.updateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.setActualPosition(Point(1,0))
        expectedPosition = Point(target.ActualPosition.X,
            target.ActualPosition.Y - target.__SPEED__.Y)
        target.motion(keysPressed)

        self.assertFalse(target.isStanding)
        self.__spriteManager__.updateSprite.assert_called_with(expectedPosition.X, expectedPosition.Y)
        
    def test_newLevel(self):
        keysPressed = []
        keysPressed.append(Key.Space)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        newMockEnviroment = MagicMock()
        newMockEnviroment.Description = "Nuevo Enviroment"
        newMockEnviroment.getStartCords = MagicMock(return_value=Point(5,5))

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.newLevel(newMockEnviroment)
        
        self.assertEqual(target.ActualPosition.X, 5*30)
        self.assertEqual(target.ActualPosition.Y, 5*30)
        self.assertFalse(target.isJumping)
        self.assertTrue(target.isGoingLeft)
        self.assertFalse(target.isGoingDown)
        self.assertTrue(target.isStanding)
        self.assertFalse(target.reachCheckpoint)
        self.assertEqual(0, target.actualImageIndex)
        self.assertNotEqual(newMockEnviroment, self.__enviroment__)

    def test_PotatoReachCheckpointFalse(self):
        keysPressed = []

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(2,5))
        target.motion(keysPressed)

        self.assertFalse(target.reachCheckpoint)

    def test_PotatoReachCheckpointTrue(self):
        keysPressed = []

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(10,1))
        target.motion(keysPressed)

        self.assertTrue(target.reachCheckpoint)

    def test_PotatoRebootScreenEnding(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.ActualPosition.X = target.__SCREEN__.X + 1
        target.ActualPosition.Y = 0

        sprite = target.motion(keysPressed)
        
        self.__spriteManager__.updateSprite.assert_called_with(0, target.ActualPosition.Y)

    def test_PotatoRebootScreenStart(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.ActualPosition.X = 0
        target.ActualPosition.Y = 0

        sprite = target.motion(keysPressed)

        self.__spriteManager__.updateSprite.assert_called_with(600, target.ActualPosition.Y)

    def test_PotatoDie(self):
        keysPressed = []

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,20))
        target.isJumping = True
        target.isGoingDown = True
        
        target.motion(keysPressed)

        self.assertEqual(Point(0,30), target.ActualPosition)

    def test_PotatoInitializeJumpWhenJumping(self):
        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.isJumping = True
        expectedStartJumpingCord = target.startJumpingCord

        target.jumpInitialize()

        self.assertTrue(target.isJumping)
        self.assertEqual(expectedStartJumpingCord, target.startJumpingCord)

    def test_PotatoInitializeJumpWhenNotJumping(self):
        expectedStartJumpingCord = 99

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.isJumping = False
        target.ActualPosition.Y = expectedStartJumpingCord

        target.jumpInitialize()

        self.assertTrue(target.isJumping)
        self.assertEqual(expectedStartJumpingCord, target.startJumpingCord)

    def test_PotatoJumpCycle(self):
        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(3,4))

        expectedPosition = Point(target.ActualPosition.X,
            112)

        target.jumpInitialize()
        target.jump()

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition.X, actualPosition.X)
        self.assertEqual(expectedPosition.Y, actualPosition.Y)

    def test_SetPotatoActualPosition(self):
        x = 3
        y = 4

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.setActualPosition(Point(x, y))

        self.assertEqual(target.ActualPosition, Point(x*30,y*30))

    def test_ShouldNotMoveIfThereIsTileGoingRight(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(2,4))
        expectedPosition = Point(target.ActualPosition.X, target.ActualPosition.Y)

        target.motion(keysPressed)
        self.assertEqual(target.ActualPosition, expectedPosition)
        
    def test_ShouldNotMoveIfThereIsTileGoingLeft(self):
        keysPressed = []
        keysPressed.append(Key.D)

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,4))
        expectedPosition = Point(target.ActualPosition.X, target.ActualPosition.Y)

        target.motion(keysPressed)

        self.assertEqual(target.ActualPosition, expectedPosition)

    def test_PotatoShouldDescendIfThereIsNotTileBehind(self):
        keysPressed = []

        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        self.__spriteManager__.updateSpriteImage = MagicMock()
        self.__spriteManager__.updateSprite = MagicMock()
        self.__spriteManager__.flipSpriteImage = MagicMock()
        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,1))
        expectedPosition = Point(target.ActualPosition.X,
            target.ActualPosition.Y + target.__SPEED__.Y)

        target.motion(keysPressed)

        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition.Y, actualPosition.Y)
        self.assertEqual(expectedPosition, actualPosition)
        self.assertFalse(target.isStanding)
        self.assertTrue(target.isGoingDown)
        self.assertTrue(target.isJumping)

    def test_ThereIsTileBehindTrue(self):
        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,0))
        
        thereIsTileBehind = target.thereIsTileBehind()

        self.assertTrue(thereIsTileBehind)

    def test_ThereIsTileBehindFalse(self):
        self.__soundManager__.getSound = MagicMock()
        self.__spriteManager__.createSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)

        target.setActualPosition(Point(1,1))
        
        thereIsTileBehind = target.thereIsTileBehind()

        self.assertFalse(thereIsTileBehind)

if __name__ == "__main__":
    unittest.main()