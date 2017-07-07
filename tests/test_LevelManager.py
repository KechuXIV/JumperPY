#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest
import uuid

from . import MockPixelArray, getColor
from ..bin import LevelManager, Point, IImageManager, ISurfaceManager, ISpriteManager, resourcePath as rs
from mock import MagicMock, Mock, call, NonCallableMock, NonCallableMagicMock, patch


class test_LevelManager(unittest.TestCase):

	def setUp(self):
		self.imageManager = Mock(spec=IImageManager)
		self.surfaceManager = Mock(spec=ISurfaceManager)
		self.spriteManager = Mock(spec=ISpriteManager)
		self.tile = MagicMock()
		self.checkpoint = MagicMock()

		self.target = LevelManager(self.imageManager, 
			self.surfaceManager, self.spriteManager,
			self.tile, self.checkpoint)

		self.imageManagerExpects = []
		self.surfaceManagerExpects = []
		self.spriteManagerExpects = []

	def tearDown(self):
		self.assertEqual(self.imageManager.mock_calls, self.imageManagerExpects)
		self.assertEqual(self.surfaceManager.mock_calls, self.surfaceManagerExpects)
		self.assertEqual(self.spriteManager.mock_calls, self.spriteManagerExpects)

	def test_GetEnviroment(self):
		mockEnviroment = MagicMock()
		mockSurface = MagicMock()

		self.imageManager.createImage.return_value = mockSurface
		self.target._enviroment = mockEnviroment

		enviroment = self.target.getEnviroment()

		self.assertIsNotNone(enviroment)
		self.assertEqual(enviroment, mockEnviroment)

	def test_GetEnviroment_ShouldRaiseExceptionIfNotRendered(self):
		with self.assertRaises(Exception) as cm:
			enviroment = self.target.getEnviroment()

		self.assertEqual(cm.exception.message, "Level not rendered")

	def test_GetLevel(self):
		expectedLevel = rs.LEVEL_LEAP_OF_FAITH

		actualLevel = self.target.getLevel()

		self.assertEqual(actualLevel, expectedLevel)

	def test_GetRenderedLevel(self):
		self.tile.Width = 30
		self.tile.Height = 30

		pixelArray = MockPixelArray()
		sourceface = Mock()

		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = 20
		self.imageManager.getImageHeight.return_value = 12
		self.imageManager.getImageColor.side_effect = getColor
		self.surfaceManager.getSurface.return_value = sourceface

		self.imageManagerExpects.append(call.loadImage(rs.LEVEL_LEAP_OF_FAITH))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())
		self.imageManagerExpects.append(call.getImageColor(0, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(255, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(76, 255, 0))

		for i in range(0,240):
			self.imageManagerExpects.append(call.getPixelArrayItemColor(5))

		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.surfaceManagerExpects.append(call.createSurface(30*20, 30*12))
		self.surfaceManagerExpects.append(call.getSurface())
		self.spriteManagerExpects.append(call.createSpriteFromSurface(0, 0, 600, 360, sourceface))
		self.spriteManagerExpects.append(call.getSprite())

		renderedLevel = self.target.getRenderedLevel()

		self.assertIsNotNone(renderedLevel)

	def test_GoToNextLevel(self):
		self.tile.Width = 30
		self.tile.Height = 30

		pixelArray = MockPixelArray()
		sourceface = Mock()

		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = 20
		self.imageManager.getImageHeight.return_value = 12
		self.imageManager.getImageColor.side_effect = getColor
		self.surfaceManager.getSurface.return_value = sourceface

		self.surfaceManagerExpects.append(call.createSurface(30*20, 30*12))
		self.surfaceManagerExpects.append(call.getSurface())
		self.spriteManagerExpects.append(call.updateSpriteFromSurface(0, 0, 600, 360, sourceface))
		self.spriteManagerExpects.append(call.getSprite())

		self.imageManagerExpects.append(call.loadImage(rs.LEVEL_JUMPERING))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())
		self.imageManagerExpects.append(call.getImageColor(0, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(255, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(76, 255, 0))

		for i in range(0,240):
			self.imageManagerExpects.append(call.getPixelArrayItemColor(5))

		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())

		renderedLevel = self.target.goToNextLevel()

		self.assertIsNotNone(renderedLevel)

	def test_getLevelSprites(self):
		self.tile.Width = 30
		self.tile.Height = 30

		pixelArray = MockPixelArray()
		sourceface = Mock()
		sprite = str(uuid.uuid4())
		image = str(uuid.uuid4())

		self.imageManager.getPixelArray.return_value = pixelArray
		self.imageManager.getImageWidth.return_value = 20
		self.imageManager.getImageHeight.return_value = 12
		self.imageManager.getImageColor.side_effect = getColor
		self.imageManager.getPixelArrayItemColor.return_value = "Black"

		self.spriteManager.createNewSprite.return_value = sprite
		self.imageManager.createImage.return_value = image

		self.imageManagerExpects.append(call.loadImage(rs.LEVEL_LEAP_OF_FAITH))
		self.imageManagerExpects.append(call.getImageWidth())
		self.imageManagerExpects.append(call.getImageHeight())
		self.imageManagerExpects.append(call.getPixelArray())
		self.imageManagerExpects.append(call.getImageColor(0, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(255, 0, 0))
		self.imageManagerExpects.append(call.getImageColor(76, 255, 0))

		for x in range(0,20):
			for y in range(0,12):
				self.imageManagerExpects.append(call.getPixelArrayItemColor(5))
				self.imageManagerExpects.append(call
					.createImage(30, 30, rs.TILE_IMAGE))
				self.spriteManagerExpects.append(call
					.createNewSprite(x*30, y*30, 30, 30, image))

		tiles = self.target.getLevelSprites()

		for tile in tiles:
			self.assertEqual(tile.Sprite, sprite)
