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
sountrack.play(-1)

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
allSprites.add(introSprite)

tilesGroup = pygame.sprite.Group()
checkpointGroup = pygame.sprite.Group()
for checkpoint in enviroment.getCheckpoints(): checkpointGroup.add(checkpoint.Sprite)
for tile in enviroment.getTiles(): tilesGroup.add(tile.Sprite)
pygameCollisionManager.setGroups(potatoSprite, tilesGroup, checkpointGroup)

clock = pygame.time.Clock()

FPS = 60

def CheckQuitEvent():
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

def Draw():
	ClearScreen()
	allSprites.draw(screen)
	#DrawLines()
	UpdateWindow()

def DrawLines():
	x = 0 
	y = 0

	pygame.draw.line(screen, (0, 200, 200), (0, 0), (600, x), (1))
	pygame.draw.line(screen, (0, 200, 200), (0, 0), (x, 480), (1))

	for i in xrange(1,40):
		x += 15
		y += 15
		pygame.draw.line(screen, (0, 200, 200), (0, y), (600, x), (1))
		pygame.draw.line(screen, (0, 200, 200), (x, 0), (x, 480), (1))

def ClearScreen():
	screen.fill((0,0,0))

def UpdateWindow():
	pygame.display.flip()

def startGame():
	intro.gameStart = True
	allSprites.remove(introSprite)
	allSprites.add(tilesGroup)
	allSprites.add(potatoSprite)
	allSprites.add(checkpointGroup)

def Logic():
	keys = pygame.key.get_pressed()

	if(not intro.gameStart):
		if(keys[pygame.K_RETURN]):
			startGame()		
	else:
		keysPressed = []

		if(keys[pygame.K_d]):
			keysPressed.append(Key.D)
		if(keys[pygame.K_a]):
			keysPressed.append(Key.A)
		if(keys[pygame.K_SPACE]):
			keysPressed.append(Key.Space)

		potato.motion(keysPressed)

		if(potato.reachCheckpoint):

			allSprites.remove(checkpointGroup)
			allSprites.remove(tilesGroup)

			tilesGroup.empty()
			checkpointGroup.empty()

			enviroment = levelManager.goToNextLevel()

			for checkpoint in enviroment.getCheckpoints(): checkpointGroup.add(checkpoint.Sprite)
			for tile in enviroment.getTiles(): tilesGroup.add(tile.Sprite)

			allSprites.add(checkpointGroup)
			allSprites.add(tilesGroup)

			pygameCollisionManager.setGroups(potatoSprite, tilesGroup, checkpointGroup)

			potato.newLevel(enviroment)

while True:
	tracer.cls()
	CheckQuitEvent()
	Logic()
	Draw()
	clock.tick(FPS)