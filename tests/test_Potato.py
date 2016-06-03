#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

#sys.path.append(os.path.abspath(os.path.join('bin')))
#sys.path.append(os.path.abspath(os.path.join('..','bin')))

from ..bin import Enviroment, Key, Point, Potato, ISoundManager, ISpriteManager, NullTracer
from mock import Mock, MagicMock, call, NonCallableMock


class test_Potato(unittest.TestCase):

    def setUp(self):
        self.screen = Point(600, 300)
        self.spriteManager = Mock(spec=ISpriteManager)
        self.enviroment = Mock(spec=Enviroment)
        self.soundManager = Mock(spec=ISoundManager)
        self.trace = NullTracer()
        
        startCords = Point(0,0)
        self.enviroment.getStartCords.return_value = startCords
        
        self.target = Potato(self.screen, self.spriteManager, 
            self.enviroment, self.soundManager, self.trace)
        
        pathDeathSound = os.path.join('..', 'bin','Resources', 'sounds', 'death.wav')
        pathJumpSound = os.path.join('..', 'bin','Resources', 'sounds', 'jump.wav')
        pathCheckpointSound = os.path.join('..', 'bin','Resources', 'sounds', 'checkpoint.wav')
        
        self.enviromentExpected = []
        self.spriteManagerExpected = []
        self.soundManagerExpected = [call.getSound(pathDeathSound), 
            call.getSound(pathJumpSound), 
            call.getSound(pathCheckpointSound)]
        
    def tearDown(self):
        self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpected)
        self.assertEqual(self.enviroment.mock_calls, self.enviromentExpected)
        self.assertEqual(self.soundManager.mock_calls, self.soundManagerExpected)

    def test_GetPotatoSprite(self):
        spriteMock = NonCallableMock()
        
        self.spriteManager.getSprite.return_value = spriteMock
        
        sprite = self.target.getSprite()

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, '../bin/Resources/potatoStanding.png'))
        self.spriteManagerExpected.append(call.getSprite())
        self.enviromentExpected.append(call.getStartCords())
    
        self.assertIsNotNone(spriteMock)
        self.assertEqual(sprite, spriteMock)

    def test_MovePotatoLeftInTheEdgeOfTheScreen(self):
        startCord = Point(0,0)
        expectedPosition = Point(600, 0)

        self.enviroment.isTile.side_effect = [False, True, True]

        keysPressed = [Key.A]

        self.target.setActualPosition(startCord)
        self.target.motion(keysPressed)
        
        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(-1,0)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(20,1)))

        self.assertTrue(self.target.isGoingLeft)
        self.assertFalse(self.target.isStanding)

    def test_MovePotatoRightInTheEdgeOfTheScreen(self):
        startCord = Point(20,0)
        expectedPosition = Point(0, 0)
        
        self.enviroment.isTile.side_effect = [False, True]

        keysPressed = [Key.D]

        self.target.setActualPosition(startCord)
        self.target.motion(keysPressed)
        
        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.flipSpriteImage())
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(21,0)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(0,1)))
        
        self.assertFalse(self.target.isGoingLeft)
        self.assertFalse(self.target.isStanding)

    def test_MovePotato(self):
        startPosition = Point(1,0)
        keysPressed = []
        
        self.enviroment.isTile.side_effect = [True]
        
        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSprite(startPosition.X*30, startPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(1,1)))
        
        self.target.setActualPosition(startPosition)
        self.target.motion(keysPressed)

        self.assertTrue(self.target.isStanding)

    def test_MovePotatoJump(self):
        keysPressed = [Key.Space]
        startPosition = Point(1,0)
        expectedPosition = Point(startPosition.X*30, -8)
            
        self.enviroment.isTile.side_effect = [False, True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoJumping.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(1,0)))
        
        self.soundManagerExpected.append(call.getSound().play())

        self.target.setActualPosition(startPosition)
        self.target.motion(keysPressed)

        self.assertFalse(self.target.isStanding)

    def test_MovePotatoLeft(self):
        keysPressed = [Key.A]
        startPosition = Point(1,0)
        expectedPosition = Point(26, startPosition.Y)
        
        self.enviroment.isTile.side_effect = [False, True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(0,0)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(1,1)))
        
        self.target.setActualPosition(startPosition)
        self.target.isGoingLeft = False
        self.target.motion(keysPressed)

        self.assertTrue(self.target.isGoingLeft)
        self.assertFalse(self.target.isStanding)

    def test_MovePotatoRight(self):
        keysPressed = [Key.D]
        startPosition = Point(1,0)
        expectedPosition = Point(startPosition.X*30 + self.target.__SPEED__.X,
            startPosition.Y)
            
        self.enviroment.isTile.side_effect = [False, True]
        
        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.flipSpriteImage())
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(2,0)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(1,1)))

        self.target.setActualPosition(startPosition)
        self.target.isGoingRight = True
        self.target.motion(keysPressed)

        self.assertFalse(self.target.isGoingLeft)
        self.assertFalse(self.target.isStanding)
        
    def test_NewLevel(self):
        startPosition = Point(1,0)
        newLevelStartCords = Point(5,5)
        expectedPosition = Point(newLevelStartCords.X*30, newLevelStartCords.Y*30)

        newMockEnviroment = Mock(spec=Enviroment)
        newMockEnviroment.getStartCords.return_value = newLevelStartCords

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.enviromentExpected.append(call.getStartCords())

        self.target.setActualPosition(startPosition)
        self.target.newLevel(newMockEnviroment)
        
        self.assertEqual(self.target.ActualPosition, expectedPosition)
        self.assertFalse(self.target.isJumping)
        self.assertTrue(self.target.isGoingLeft)
        self.assertFalse(self.target.isGoingDown)
        self.assertTrue(self.target.isStanding)
        self.assertFalse(self.target.reachCheckpoint)
        self.assertEqual(0, self.target.actualImageIndex)
        self.assertNotEqual(newMockEnviroment, self.enviroment)

    def test_PotatoReachCheckpointFalse(self):
        startPosition = Point(2,5)
        expectedPosition = Point(startPosition.X*30,startPosition.Y*30)
        keysPressed = []

        self.enviroment.isTile.side_effect = [True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, 
            os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(
            os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, 
            expectedPosition.Y))

        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(2,6)))

        self.target.setActualPosition(startPosition)
        self.target.motion(keysPressed)

        self.assertFalse(self.target.reachCheckpoint)

    def test_PotatoReachCheckpointTrue(self):
        startPosition = Point(10,1)
        finishCord = startPosition
        expectedPosition = Point(startPosition.X*30,startPosition.Y*30)
        keysPressed = []

        self.enviroment.getFinishCords.return_value = finishCord
        self.enviroment.isTile.side_effect = [True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, 
            os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(
            os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, 
            expectedPosition.Y))

        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(10,2)))
        
        self.soundManagerExpected.append(call.getSound().play())

        self.target.setActualPosition(startPosition)
        self.target.motion(keysPressed)

        self.assertTrue(self.target.reachCheckpoint)

    def test_PotatoDie(self):
        startPosition = Point(1,20)
        startCords = Point(0,1)
        expectedPosition = Point(startCords.X*30,startCords.Y*30)
        keysPressed = []
        
        self.enviroment.getStartCords.return_value = startCords
        self.enviroment.isTile.side_effect = [False]
        
        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, 
            os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(
            os.path.join('..', 'bin','Resources', 'potatoJumping.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, 
            expectedPosition.Y))
            
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(1,21)))
        self.enviromentExpected.append(call.getStartCords())
        
        self.soundManagerExpected.append(call.getSound().play())

        self.target.setActualPosition(startPosition)
        self.target.isJumping = True
        self.target.isGoingDown = True
        
        self.target.motion(keysPressed)

        self.assertEqual(expectedPosition, self.target.ActualPosition)

    def test_ShouldNotMoveIfThereIsTileGoingLeft(self):
        startPosition = Point(2,4)
        expectedPosition = Point(64, startPosition.Y*30)
        keysPressed = [Key.D]
        
        self.enviroment.isTile.side_effect = [False, True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.flipSpriteImage())
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(3,4)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(2,5)))

        self.target.setActualPosition(startPosition)

        self.target.motion(keysPressed)
        
        self.assertEqual(self.target.ActualPosition, expectedPosition)

    def test_ShouldNotMoveIfThereIsTileGoingRight(self):
        startPosition = Point(2,4)
        expectedPosition = Point(56, startPosition.Y*30)
        keysPressed = [Key.A]
        
        self.enviroment.isTile.side_effect = [False, True]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoWalking.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.isTile(Point(1,4)))
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(2,5)))

        self.target.setActualPosition(startPosition)

        self.target.motion(keysPressed)
        
        self.assertEqual(self.target.ActualPosition, expectedPosition)
        
    def test_PotatoShouldDescendIfThereIsNotTileBehind(self):
        startPosition = Point(2,4)
        expectedPosition = Point(60, 128)
        keysPressed = []
        
        self.enviroment.isTile.side_effect = [False, False]

        self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30, os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSpriteImage(os.path.join('..', 'bin','Resources', 'potatoStanding.png')))
        self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
        
        self.enviromentExpected.append(call.getStartCords())
        self.enviromentExpected.append(call.getFinishCords())
        self.enviromentExpected.append(call.isTile(Point(2,5)))
        self.enviromentExpected.append(call.isTile(Point(2,5)))
        
        self.soundManagerExpected.append(call.getSound().play())

        self.target.setActualPosition(startPosition)

        self.target.motion(keysPressed)
        
        self.assertEqual(self.target.ActualPosition, expectedPosition)
        self.assertFalse(self.target.isStanding)
        self.assertTrue(self.target.isGoingDown)
        self.assertTrue(self.target.isJumping)

if __name__ == "__main__":
    unittest.main()