#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GameElement(object):

	def __init__(self, spriteManager, soundManager, enviroment, screenCords, measure):
		self.__screenCords = screenCords
		self._spriteManager = spriteManager
		self._soundManager = soundManager
		self._measure = measure

	def _getSound(self, path):
		return self._soundManager.getSound(path)

	def _getSprite(self):
		return self._spriteManager.getSprite()

	def _createSprite(self, position):
		self._spriteManager.createSprite(position.X, position.Y, 
			self._measure.X, self._measure.Y)

	def __flipSpriteImage(self):
		return self._spriteManager.flipSpriteImage()

	def _updateImage(self, imagePath, isGoingLeft):
		self.__updateSpriteImage(imagePath)
		if(not isGoingLeft):
			self.__flipSpriteImage()

	def __updateSpriteImage(self, imagePath):
		return self._spriteManager.updateSpriteImage(imagePath)

	def _updateSpritePosition(self, position):
		return self._spriteManager.updateSprite(position.X, position.Y)