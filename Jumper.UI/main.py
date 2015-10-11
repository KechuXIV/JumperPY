# -*- coding: utf-8 -*-
import pygame
import os
import sys

lib_path = os.path.abspath(os.path.join('..', 'Jumper.Core'))
sys.path.append(lib_path)

from Potato import *
from Point import *
from Key import *
from PygameSpriteManager import *
from LevelManager import *


pygame.init()
screenCords = Point(600, 300)
screen = pygame.display.set_mode((screenCords.X, screenCords.Y))
pygameSpriteManager = PygameSpriteManager()
levelManager = LevelManager() 
potato = Potato(screenCords,pygameSpriteManager)

allSprites = pygame.sprite.Group()
allSprites.add(levelManager.GetRenderedLevel())
allSprites.add(potato.GetSprite())

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

while True:
	CheckQuitEvent()

	Logic()

	Draw()

	clock.tick(FPS)