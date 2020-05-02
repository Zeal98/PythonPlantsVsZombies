import pygame as pg
from pygame.locals import *
from Object.py import *

class ZombieObj():
	def __init__(self, type, time, offsetY):
		self.type = type;
		self.time = time;
		self.offsetY = offsetY

class LevelEditor():
	def __init__(self):
		self.zombieList = list()
		self.objList = list()
		self.time = 0.0
		
		self.selectedZombie = None
	
		self.screen = pg.display.set_mode((600, 500))
		pg.display.set_caption("Level Editor")
		
	def update(self):
		while True:
			for event in pg.event.get():
				if event.type in (QUIT):
					pg.quit()
					sys.exit()
			self.screen.fill((0, 0, 200))
			for obj in self.objList:
				self.screen.blit(obj.image, (obj.posX, obj.posY))
			pg.display.update()

	def addObj(self, obj, posX=None, posY=None):
		if(posX != None):
			obj.posX = posX
		if(posY != None):
			obj.posY = posY
		self.objList.append(obj)
	def addZombie(self):
		self.zombieList.append((self.selectedZombie, self.time))
