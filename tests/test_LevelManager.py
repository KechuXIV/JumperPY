#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest
import uuid

from itertools import chain, cycle
from . import MockPixelArray
from ..bin import LevelManager, Point, IImageManager, ISurfaceManager, ISpriteManager, resourcePath as rs
from mock import MagicMock, Mock, call, NonCallableMock, NonCallableMagicMock, patch


class test_LevelManager(unittest.TestCase):

	def setUp(self):
		self.imageManager = Mock(spec=IImageManager)
		self.surfaceManager = Mock(spec=ISurfaceManager)
		self.spriteManager = Mock(spec=ISpriteManager)

		self.imageManager.getColor.side_effect = ["Black", "Red", "Green"]

		self.target = LevelManager(self.imageManager, 
			self.surfaceManager, self.spriteManager)

		self.imageManagerExpects = [call.getColor(0, 0, 0, 255), 
			call.getColor(0, 0, 255, 255),
			call.getColor(0, 255, 76, 255)]

		self.surfaceManagerExpects = []
		self.spriteManagerExpects = []

	def tearDown(self):
		self.assertEqual(self.imageManager.mock_calls, self.imageManagerExpects)
		self.assertEqual(self.surfaceManager.mock_calls, self.surfaceManagerExpects)
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpects)

	def test_GetLevel(self):
		expectedLevel = rs.LEVEL_LEAP_OF_FAITH

		actualLevel = self.target.getLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GoToNextLevel(self):
		imageWidth = 5
		imageHeight = 3
		expectedStarCord = Point(0, 2)

		pixelArray = MockPixelArray()
		sourceface = Mock()
		spriteTile = str(uuid.uuid4())
		spriteCheckpoint = str(uuid.uuid4())
		imageCheckpoint = str(uuid.uuid4())
		imageTile = str(uuid.uuid4())

		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = imageWidth
		self.imageManager.getImageHeight.return_value = imageHeight
		self.imageManager.getPixelArrayItemColor.side_effect=chain(['Green','Green','Red'], cycle(['Black']))

		self.spriteManager.createNewSprite.side_effect = chain([spriteCheckpoint, spriteCheckpoint], cycle([spriteTile]))
		self.imageManager.createImage.return_value = imageCheckpoint
		self.imageManager.createImage.return_value = imageTile
		self.imageManager.createImage.side_effect=chain([imageCheckpoint, imageCheckpoint], cycle([imageTile]))

		self.imageManagerExpects.append(call.loadImage(rs.LEVEL_JUMPERING))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())


		for j in range(0,2):
			self.imageManagerExpects.append(call
					.getPixelArrayItemColor(5))
			self.imageManagerExpects.append(call
					.createImage(30, 30, rs.CHECKPOINT_IMAGE))
			self.spriteManagerExpects.append(call
					.createNewSprite(0, j*30, 30, 30, imageCheckpoint))

		for x in range(0,imageWidth):
			for y in range(0,imageHeight):
				if(x != 0 or y > 1):
					self.imageManagerExpects.append(call.getPixelArrayItemColor(5))
				if(x != 0 or y > 2):
					self.imageManagerExpects.append(call
						.createImage(30, 30, rs.TILE_IMAGE))
					self.spriteManagerExpects.append(call
						.createNewSprite(x*30, y*30, 30, 30, imageTile))

		enviroment = self.target.goToNextLevel()

		for tile in enviroment.getTiles():
			self.assertEqual(tile.Sprite, spriteTile)

		for checkpoint in enviroment.getCheckpoints():
			self.assertEqual(checkpoint.Sprite, spriteCheckpoint)

		self.assertEqual(enviroment.getStartCords(), expectedStarCord)

	def test_getLevelSprites(self):
		imageWidth = 5
		imageHeight = 3
		expectedStarCord = Point(0, 2)

		pixelArray = MockPixelArray()
		sourceface = Mock()
		spriteTile = str(uuid.uuid4())
		spriteCheckpoint = str(uuid.uuid4())
		imageCheckpoint = str(uuid.uuid4())
		imageTile = str(uuid.uuid4())

		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = imageWidth
		self.imageManager.getImageHeight.return_value = imageHeight
		self.imageManager.getPixelArrayItemColor.side_effect=chain(['Green','Green','Red'], cycle(['Black']))

		self.spriteManager.createNewSprite.side_effect = chain([spriteCheckpoint, spriteCheckpoint], cycle([spriteTile]))
		self.imageManager.createImage.return_value = imageCheckpoint
		self.imageManager.createImage.return_value = imageTile
		self.imageManager.createImage.side_effect=chain([imageCheckpoint, imageCheckpoint], cycle([imageTile]))

		self.imageManagerExpects.append(call.loadImage(rs.LEVEL_LEAP_OF_FAITH))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())


		for j in range(0,2):
			self.imageManagerExpects.append(call.getPixelArrayItemColor(5))
			self.imageManagerExpects.append(call
				.createImage(30, 30, rs.CHECKPOINT_IMAGE))
			self.spriteManagerExpects.append(call
				.createNewSprite(0, j*30, 30, 30, imageCheckpoint))

		for x in range(0,imageWidth):
			for y in range(0,imageHeight):
				if(x != 0 or y > 1):
					self.imageManagerExpects.append(call.getPixelArrayItemColor(5))
				if(x != 0 or y > 2):
					self.imageManagerExpects.append(call
						.createImage(30, 30, rs.TILE_IMAGE))
					self.spriteManagerExpects.append(call
						.createNewSprite(x*30, y*30, 30, 30, imageTile))

		enviroment = self.target.getEnviroment()

		for tile in enviroment.getTiles():
			self.assertEqual(tile.Sprite, spriteTile)

		for checkpoint in enviroment.getCheckpoints():
			self.assertEqual(checkpoint.Sprite, spriteCheckpoint)

		self.assertEqual(enviroment.getStartCords(), expectedStarCord)
