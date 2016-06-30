#!/usr/bin/env python
# -*- coding: utf-8 -*-


class gameElement(object):

	def __init__(self, spriteManager, soundManager, enviroment, screenCords):
		super(gameElement, self).__init__()
		self._spriteManager = spriteManager
		self._soundManager = soundManager
		self._enviroment = enviroment
		self._screenCords = screenCords
