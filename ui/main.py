#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import Checkpoint, Intro, Key, LevelManager, Point, Potato, Tile, Tracer, NullTracer, resourcePath as rs
from pygameImageManager import PygameImageManager
from pygameSoundManager import PygameSoundManager
from pygameSpriteManager import PygameSpriteManager
from pygameSurfaceManager import PygameSurfaceManager
from pygameCollisionManager import PygameCollisionManager


pygame.init()
sountrack = pygame.mixer.Sound(rs.SOUNDTRACK)
#sountrack.play(-1)

screenCords = Point(600, 360)
screen = pygame.display.set_mode((screenCords.X, screenCords.Y))
pygame.display.set_caption("JumperPY")

pygameSoundManager = PygameSoundManager()
potatoPygameSpriteManager = PygameSpriteManager()
levelManagerPygameSpriteManager = PygameSpriteManager()
blockPygameSpriteManager = PygameSpriteManager()
introPygameSpriteManager = PygameSpriteManager()
pygameImageManager = PygameImageManager()
pygameSourceManager = PygameSurfaceManager()
pygameCollisionManager = PygameCollisionManager()

levelManager = LevelManager(pygameImageManager, pygameSourceManager, levelManagerPygameSpriteManager)
enviroment = levelManager.getEnviroment()

tracer = NullTracer()
potato = Potato(screenCords, potatoPygameSpriteManager, enviroment, pygameSoundManager, pygameCollisionManager, tracer)
intro = Intro(screenCords, introPygameSpriteManager)

introSprite = intro.getSprite()
potatoSprite = potato.getSprite()

allSprites = pygame.sprite.Group()
tilesGroup = pygame.sprite.Group()
checkpointGroup = pygame.sprite.Group()

allSprites.add(introSprite)

clock = pygame.time.Clock()

FPS = 60

def checkQuitEvent():
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

def draw():
	clearScreen()
	allSprites.draw(screen)
	updateWindow()

def clearScreen():
	screen.fill((0,0,0))

def updateWindow():
	pygame.display.flip()

def startGame():
	intro.gameStart = True
	allSprites.remove(introSprite)
	setEnviromentGroups(enviroment)
	allSprites.add(potatoSprite)

def getPressedKeys():
	keys = pygame.key.get_pressed()
	keysPressed = []

	if(keys[pygame.K_d]):
		keysPressed.append(Key.D)
	if(keys[pygame.K_a]):
		keysPressed.append(Key.A)
	if(keys[pygame.K_SPACE]):
		keysPressed.append(Key.Space)

	return keysPressed

def removeEnviromentGroups():
	allSprites.remove(checkpointGroup)
	allSprites.remove(tilesGroup)

	tilesGroup.empty()
	checkpointGroup.empty()

def setEnviromentGroups(enviroment):
	for checkpoint in enviroment.getCheckpoints(): checkpointGroup.add(checkpoint.Sprite)
	for tile in enviroment.getTiles(): tilesGroup.add(tile.Sprite)

	allSprites.add(checkpointGroup)
	allSprites.add(tilesGroup)

	pygameCollisionManager.setGroups(potatoSprite, tilesGroup, checkpointGroup)

def goToNextLevel():
	removeEnviromentGroups()

	enviroment = levelManager.goToNextLevel()
	setEnviromentGroups(enviroment)

	potato.newLevel(enviroment)

def logic():
	if(not intro.gameStart):
		if(pygame.key.get_pressed()[pygame.K_RETURN]):
			startGame()
	elif(potato.motion(getPressedKeys())):
		goToNextLevel()

while True:
	tracer.cls()
	checkQuitEvent()
	logic()
	draw()
	clock.tick(FPS)