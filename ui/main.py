#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

from ..bin import Checkpoint, Intro, Key, LevelManager, Point, Potato, Tile, Tracer
from PygameImageManager import PygameImageManager
from PygameSoundManager import PygameSoundManager
from PygameSpriteManager import PygameSpriteManager
from PygameSurfaceManager import PygameSurfaceManager
from Tracer import Tracer


pygame.init()
sountrack = pygame.mixer.Sound(os.path.join('..', 'bin','Resources', 'sounds', 'killingtime.ogg'))
#sountrack.play(-1)

screenCords = Point(600, 360)
screen = pygame.display.set_mode((screenCords.X, screenCords.Y))

pygameSoundManager = PygameSoundManager()
potatoPygameSpriteManager = PygameSpriteManager()
pygameImageManager = PygameImageManager()
pygameSourceManager = PygameSurfaceManager()

checkpoint = Checkpoint(pygameImageManager)
levelManagerPygameSpriteManager = PygameSpriteManager()
tile = Tile(pygameImageManager)

levelManager = LevelManager(pygameImageManager, pygameSourceManager, levelManagerPygameSpriteManager, tile, checkpoint)
levelSprite = levelManager.getRenderedLevel()
enviroment = levelManager.getEnviroment()
tracer = Tracer()
potato = Potato(screenCords, potatoPygameSpriteManager, enviroment, pygameSoundManager, tracer)
intro = Intro(screenCords, potatoPygameSpriteManager)


gameStart = False

allSprites = pygame.sprite.Group()
allSprites.add(intro)

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
#	DrawLines()
	UpdateWindow()

def DrawLines():
	x = 0 
	y = 0

	pygame.draw.line(screen, (0, 200, 200), (0, 0), (600, x), (1))
	pygame.draw.line(screen, (0, 200, 200), (0, 0), (x, 300), (1))

	for i in xrange(1,40):
		x += 15
		y += 15

		pygame.draw.line(screen, (0, 200, 200), (0, y), (600, x), (1))
		pygame.draw.line(screen, (0, 200, 200), (x, 0), (x, 300), (1))

	pygame.display.flip()

def ClearScreen():
	screen.fill((0,0,0))

def UpdateWindow():
	pygame.display.flip()
	
def startGame():
	gameStart = True
	allSprites = pygame.sprite.Group()
	allSprites.add(potato.getSprite())
	allSprites.add(levelSprite)

def Logic():
	keys = pygame.key.get_pressed()

	if(not gameStart):
		if(keys[pygame.K_SPACE]):
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
			levelManager.goToNextLevel()
			enviroment = levelManager.getEnviroment()
			potato.newLevel(enviroment)

while True:
	tracer.cls()

	CheckQuitEvent()

	Logic()

	Draw()

	clock.tick(FPS)