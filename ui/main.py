# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'bin'))
sys.path.append(lib_path)

from Potato import *
from LevelManager import *
from Point import *
from Key import *

from PygameSpriteManager import *
from PygameImageManager import *
from PygameSurfaceManager import *
from PygameSoundManager import *


pygame.init()
sountrack = pygame.mixer.Sound(os.path.join('..', 'bin','Resources', 'sounds', 'killingtime.ogg'))
sountrack.play(-1)

screenCords = Point(600, 300)
screen = pygame.display.set_mode((screenCords.X, screenCords.Y))

pygameSoundManager = PygameSoundManager()

levelManagerPygameSpriteManager = PygameSpriteManager()
potatoPygameSpriteManager = PygameSpriteManager()

pygameImageManager = PygameImageManager()
pygameSourceManager = PygameSurfaceManager()

levelManager = LevelManager(pygameImageManager, pygameSourceManager, levelManagerPygameSpriteManager)
levelSprite = levelManager.GetRenderedLevel()
enviroment = levelManager.GetEnviroment()

potato = Potato(screenCords, potatoPygameSpriteManager, enviroment, pygameSoundManager)

allSprites = pygame.sprite.Group()
allSprites.add(potato.GetSprite())
allSprites.add(levelSprite)

clock = pygame.time.Clock()

FPS = 10

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

def Logic():
	keys = pygame.key.get_pressed()

	keysPressed = []

	if(keys[pygame.K_d]):
		keysPressed.append(Key.D)
	if(keys[pygame.K_a]):
		keysPressed.append(Key.A)
	if(keys[pygame.K_SPACE]):
		keysPressed.append(Key.Space)

	potato.Motion(keysPressed)
	if(potato.reachCheckpoint):
		levelManager.GoToNextLevel()
		enviroment = levelManager.GetEnviroment()
		potato.NewLevel(enviroment)

while True:
	CheckQuitEvent()

	Logic()

	Draw()

	clock.tick(FPS)