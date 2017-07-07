#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

from mock import Mock, MagicMock, call, NonCallableMock
from ..bin import Enviroment, Key, Point, Position, Potato, ISoundManager, ISpriteManager, ICollisionManager, NullTracer


class test_Potato(unittest.TestCase):

	def setUp(self):
		self.screen = Point(600, 300)
		self.spriteManager = Mock(spec=ISpriteManager)
		self.enviroment = Mock(spec=Enviroment)
		self.soundManager = Mock(spec=ISoundManager)
		self.collisionManager = Mock(spec=ICollisionManager)
		self.trace = NullTracer()

		startCords = Point(0,0)
		self.enviroment.getStartCords.return_value = startCords

		self.target = Potato(self.screen, self.spriteManager,
			self.enviroment, self.soundManager,
			self.collisionManager, self.trace)

		pathDeathSound = os.path.join('JumperPY', 'bin','Resources', 'sounds', 'death.wav')
		pathJumpSound = os.path.join('JumperPY', 'bin','Resources', 'sounds', 'jump.wav')
		pathCheckpointSound = os.path.join('JumperPY', 'bin','Resources', 'sounds', 'checkpoint.wav')

		self.spriteManagerExpected = []
		self.spriteManagerExpected.append(call.createSprite(0, 0, 30, 30))
		self.enviromentExpected = [call.getStartCords()]
		self.soundManagerExpected = [call.getSound(pathDeathSound),
			call.getSound(pathJumpSound), 
			call.getSound(pathCheckpointSound)]
		self.collisionManagerExpected = []

	def tearDown(self):
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpected)
		self.assertEqual(self.enviroment.mock_calls, self.enviromentExpected)
		self.assertEqual(self.soundManager.mock_calls, self.soundManagerExpected)
		self.assertEqual(self.collisionManager.mock_calls, self.collisionManagerExpected)

	def test_GetPotatoSprite(self):
		spriteMock = NonCallableMock()

		self.spriteManager.getSprite.return_value = spriteMock

		sprite = self.target.getSprite()

		self.spriteManagerExpected.append(call.getSprite())

		self.assertIsNotNone(spriteMock)
		self.assertEqual(sprite, spriteMock)

	def test_MovePotatoLeftInTheEdgeOfTheScreen(self):
		startCord = Point(0,0)
		expectedPosition = Point(600, 0)
		keysPressed = [Key.A]
		collision = { Position.BEHIND : True, Position.LEFT : False }

		self.collisionManager.getCollisions.return_value = collision

		self.target.setActualPosition(startCord)
		self.target.motion(keysPressed)

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.collisionManagerExpected.append(call.getCollisions())

		self.assertTrue(self.target.isGoingLeft)
		self.assertFalse(self.target.isStanding)

	def test_MovePotatoRightInTheEdgeOfTheScreen(self):
		startCord = Point(20,0)
		expectedPosition = Point(0, 0)
		collision = { Position.BEHIND : True, Position.RIGHT : False }
		keysPressed = [Key.D]

		self.collisionManager.getCollisions.return_value = collision

		self.target.setActualPosition(startCord)
		self.target.motion(keysPressed)

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())

		self.assertFalse(self.target.isGoingLeft)
		self.assertFalse(self.target.isStanding)

	def test_MovePotato(self):
		startPosition = Point(1,0)
		keysPressed = []
		collision = { Position.BEHIND : True }

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoStanding.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(startPosition.X*30, startPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertTrue(self.target.isStanding)

	def test_MovePotatoJump(self):
		keysPressed = [Key.Space]
		startPosition = Point(1,0)
		expectedPosition = Point(startPosition.X*30, -8)

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoJumping.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.soundManagerExpected.append(call.getSound().play())
		self.collisionManagerExpected.append(call.getCollisions())
		
		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertFalse(self.target.isStanding)

	def test_MovePotatoLeft(self):
		startPosition = Point(1,0)
		expectedPosition = Point(startPosition.X*30 - 4, startPosition.Y)
		collision = { Position.BEHIND : True, Position.LEFT : False }
		keysPressed = [Key.A]

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.collisionManagerExpected.append(call.getCollisions())

		self.target.setActualPosition(startPosition)
		self.target.isGoingLeft = False
		self.target.motion(keysPressed)

		self.assertTrue(self.target.isGoingLeft)
		self.assertFalse(self.target.isStanding)

	def test_MovePotatoRight(self):
		startPosition = Point(1,0)
		expectedPosition = Point(startPosition.X*30 + 4,
			startPosition.Y)
		collision = { Position.BEHIND : True, Position.RIGHT : False }
		keysPressed = [Key.D]

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
			os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())

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

		self.target.setActualPosition(startPosition)
		self.target.newLevel(newMockEnviroment)

		self.assertEqual(self.target.ActualPosition, expectedPosition)
		self.assertFalse(self.target.isJumping)
		self.assertFalse(self.target.isGoingLeft)
		self.assertFalse(self.target.isGoingDown)
		self.assertTrue(self.target.isStanding)
		self.assertFalse(self.target.reachCheckpoint)
		self.assertEqual(0, self.target.actualImageIndex)
		self.assertNotEqual(newMockEnviroment, self.enviroment)

	def test_PotatoReachCheckpointFalse(self):
		startPosition = Point(2,5)
		expectedPosition = Point(startPosition.X*30,startPosition.Y*30)
		collision = { Position.BEHIND : True }
		keysPressed = []

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
			os.path.join('JumperPY', 'bin','Resources', 'potatoStanding.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X,
			expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.collisionManagerExpected.append(call.getCollisions())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertFalse(self.target.reachCheckpoint)

	def test_PotatoReachCheckpointTrue(self):
		startPosition = Point(10,1)
		finishCord = startPosition
		expectedPosition = Point(startPosition.X*30,startPosition.Y*30)
		collision = { Position.BEHIND : True }
		keysPressed = []

		self.enviroment.getFinishCords.return_value = finishCord
		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
			os.path.join('JumperPY', 'bin','Resources', 'potatoStanding.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X,
			expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.soundManagerExpected.append(call.getSound().play())
		self.collisionManagerExpected.append(call.getCollisions())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertTrue(self.target.reachCheckpoint)

	def test_PotatoDie(self):
		startPosition = Point(1,20)
		startCords = Point(0,1)
		expectedPosition = Point(startCords.X*30,startCords.Y*30)
		collision = { Position.BEHIND : False }
		keysPressed = []

		self.enviroment.getStartCords.return_value = startCords
		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
			os.path.join('JumperPY', 'bin','Resources', 'potatoStanding.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X,
			expectedPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())
		self.enviromentExpected.append(call.getStartCords())

		self.soundManagerExpected.append(call.getSound().play())

		self.target.setActualPosition(startPosition)
		self.target.isJumping = True
		self.target.isGoingDown = True
		self.target.motion(keysPressed)

		self.assertEqual(expectedPosition, self.target.ActualPosition)

	def test_ShouldNotMoveIfThereIsTileGoingRight(self):
		startPosition = Point(2,4)
		expectedPosition = Point(startPosition.X*30, startPosition.Y*30)
		collision = { Position.BEHIND : True, Position.RIGHT : True }
		keysPressed = [Key.D]

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertEqual(self.target.ActualPosition, expectedPosition)

	def test_ShouldNotMoveIfThereIsTileGoingLeft(self):
		startPosition = Point(2,4)
		expectedPosition = Point(startPosition.X*30, startPosition.Y*30)
		collision = { Position.BEHIND : True, Position.LEFT : True }
		keysPressed = [Key.A]

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoWalking.png')))
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.collisionManagerExpected.append(call.getCollisions())
		self.enviromentExpected.append(call.getFinishCords())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertEqual(self.target.ActualPosition, expectedPosition)

	def test_PotatoShouldDescendIfThereIsNotTileBehind(self):
		startPosition = Point(2,4)
		expectedPosition = Point(60, 128)
		collision = { Position.BEHIND : False }
		keysPressed = []

		self.collisionManager.getCollisions.return_value = collision

		self.spriteManagerExpected.append(call.updateSpriteImage(
				os.path.join('JumperPY', 'bin','Resources', 'potatoJumping.png')))
		self.spriteManagerExpected.append(call.flipSpriteImage())
		self.spriteManagerExpected.append(call.updateSprite(expectedPosition.X, expectedPosition.Y))
		self.enviromentExpected.append(call.getFinishCords())
		self.collisionManagerExpected.append(call.getCollisions())
		self.soundManagerExpected.append(call.getSound().play())

		self.target.setActualPosition(startPosition)
		self.target.motion(keysPressed)

		self.assertEqual(self.target.ActualPosition, expectedPosition)
		self.assertFalse(self.target.isStanding)
		self.assertTrue(self.target.isGoingDown)
		self.assertTrue(self.target.isJumping)
