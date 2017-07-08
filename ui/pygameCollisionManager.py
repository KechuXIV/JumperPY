#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

from ..bin import ICollisionManager, Position


class PygameCollisionManager(ICollisionManager):

	def __init__(self):
		self._sprite = None
		self._tilesGroup = None
		self.collision = { Position.BEHIND : True,
		 Position.LEFT : False,
		 Position.RIGHT : False,
		 Position.CHECKPOINT : False}

	def setGroups(self, player, tilesGroup, checkpointGroup):
		self._sprite = player
		self._tilesGroup = tilesGroup
		self._checkpointGroup = checkpointGroup

	def getCollisions(self):
		crashgroup = pygame.sprite.spritecollide(self._sprite, self._tilesGroup, False, pygame.sprite.collide_rect)

		self.collision[Position.LEFT] = any(self._sprite.rect.left > (tile.rect.right - 6) for tile in crashgroup)
		self.collision[Position.RIGHT] = any(self._sprite.rect.right < (tile.rect.left + 6) for tile in crashgroup)

		self._sprite.rect.bottom = self._sprite.rect.bottom + 1
		crashgroup = pygame.sprite.spritecollide(self._sprite, self._tilesGroup, False, pygame.sprite.collide_rect)
		self.collision[Position.BEHIND] = any(not(self._sprite.rect.left > (tile.rect.right - 6)) and not(self._sprite.rect.right < (tile.rect.left + 6)) and (self._sprite.rect.bottom >= (tile.rect.top)) for tile in crashgroup)
		self._sprite.rect.bottom = self._sprite.rect.bottom - 1

		crashgroup = pygame.sprite.spritecollide(self._sprite, self._checkpointGroup, False, pygame.sprite.collide_rect)

		self.collision[Position.CHECKPOINT] = any(crashgroup)

		return self.collision
