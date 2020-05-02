import pygame as pg
from pygame.locals import *

class Object():
	def __init__(self, posX, posY, rangeX, rangeY, image):
		#position x,y, range x,y, filename_of_image
		self.posX = posX
		self.posY = posY
		self.rangeX = rangeX
		self.rangeY = rangeY
		self.image = image
		
		self.belongs = None

		self.isClicked = False
		self.isSelected = False
		self.loadImage()

	def isInside(self, posX, posY):
		#return true if (posX, posY) inside the object
		if (self.posX <= posX <= self.posX + self.rangeX) and (self.posY <= posY <= self.posY + self.rangeY):
			return True
		else:
			return False
	
	def loadImage(self):
		self.image = pg.image.load(self.image).convert_alpha()

	def onClick(self):
		self.isClicked = True
		
class TimeButton(Object):
	def __init__(self, posX, posY, rangeX, rangeY, image, function):
		#function: int n, means +/- n frame change per click
		super(TimeButton, self).__init__(posX, posY, rangeX, rangeY, image)
		self.function = function
	
	def loadImage(self):
		myFont = pg.font.Font(None, 60)
		self.image = myFont.render("%s"%(n), True, (255,255,255))

	def onClick(self):
		self.isClicked = True
		self.belongs.time = self.belongs.time + n

class Ground(Object):
	def __init__(self, offsetX, offsetY, originX, originY):
		self.size = 100
		super(Ground, self).__init__(originX+offsetX*self.size, originY+offsetY*self.size, self.size, self.size, 'image')
		self.offsetX = offsetX
		self.offsetY = offsetY
	def loadImage(self):
		myFont = pg.font.Font(None, self.size)
		self.image = pg.render("(%s,%s)"%(offsetX,offsetY), True, (255,255,255))
	def onClick(self):
		self.isClicked = True
		if self.belongs.selectedZombie != None:
			self.belongs.addZombie(self.offsetX, self.offsetY)
