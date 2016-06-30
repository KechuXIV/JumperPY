#!/usr/bin/env python
# -*- coding: utf-8 -*-


class gameElement(object):

	def __init__(self, spriteManager, soundManager, enviroment, screenCords):
		super(gameElement, self).__init__()
		self.__spriteManager = spriteManager
		self.__soundManager = soundManager
		self.__enviroment = enviroment
		self.__screenCords = screenCords
