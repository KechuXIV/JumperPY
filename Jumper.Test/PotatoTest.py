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
from PygameSoundManager import *
from PygameSpriteManager import *
from ISoundManager import *
from ISpriteManager import *



class PotatoTest(unittest.TestCase):

    def setUp(self):
        screenWidth = 600
        screenHeight = 300
        screen = Point(screenWidth, screenHeight)
        spriteManager = PygameSpriteManager()
        soundManager = PygameSoundManager()
        tiles = [Point(0, 1),Point(1, 1), Point(2, 1), Point(19, 1), Point(0,4), Point(2,4), Point(0,5), Point(1,5), Point(2,5)]
        startCord = Point(0, 1)
        finishCord = Point(10, 1)

        enviroment = Enviroment(startCord, finishCord, tiles)

        self.__spriteManager__ = ISpriteManager()
        self.__soundManager__ = ISoundManager()
        self.__screen__ = screen
        self.__enviroment__ = enviroment

        self.potato = Potato(screen, spriteManager, enviroment, soundManager)

    def test_GetPotatoSprite(self):
        expectedPosition = self.potato.ActualPosition

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
        expectedPosition = Point(585,
            0)

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
        self.potato.SetActualPosition(Point(1,0))
        expectedPosition = self.potato.ActualPosition
        keysPressed = []

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        self.potato.Motion(keysPressed)
        target.SetActualPosition(Point(1,0))
        actualPosition = target.ActualPosition

        self.assertEqual(expectedPosition, actualPosition)
        self.assertTrue(target.isStanding)

    def test_MovePotatoLeft(self):
        keysPressed = []
        keysPressed.append(Key.A)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock() #Tengo que hacer el assert del Expected
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

        self.__spriteManager__.UpdateSpriteImage = MagicMock() #Tengo que hacer el assert del Expected
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
        self.potato.SetActualPosition(Point(1,0))
        expectedPosition = Point(self.potato.ActualPosition.X,
            self.potato.ActualPosition.Y - self.potato.__SPEED__.Y)
        keysPressed = []
        keysPressed.append(Key.Space)

        self.__soundManager__.GetSound = MagicMock()
        self.__spriteManager__.CreateSprite = MagicMock()

        self.__spriteManager__.UpdateSpriteImage = MagicMock() #Tengo que hacer el assert del Expected
        self.__spriteManager__.FlipSpriteImage = MagicMock()
        spriteMock = MagicMock()
        spriteMock.Description = "Sprite Mockeado"
        self.__spriteManager__.UpdateSprite = MagicMock(return_value=spriteMock)

        target = Potato(self.__screen__,
            self.__spriteManager__,
            self.__enviroment__,
            self.__soundManager__)
        target.SetActualPosition(Point(1,0))
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
        self.potato.ActualPosition.X = self.potato.__SCREEN__.X

        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, 0)

    def test_PotatoCantGoOutsideFromScreenStart(self):
        self.potato.ActualPosition.X = 570

        keysPressed = []
        keysPressed.append(Key.D)

        sprite = self.potato.Motion(keysPressed)

        self.assertEqual(sprite.rect.x, 585)

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

    def test_ShouldNotMoveIfThereIsTileGoingRight(self):
        self.potato.SetActualPosition(Point(1,4))
        expectedPosition = self.potato.ActualPosition

        keysPressed = []
        keysPressed.append(Key.A)

        self.potato.Motion(keysPressed)

        self.assertEqual(self.potato.ActualPosition, expectedPosition)

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