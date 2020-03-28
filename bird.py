from setup import *
import pygame as pg

VELOCITY_UP = -12
class Bird:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vel = 0
		self.tick = 0
		self.IMGS = GFX['bird']
		self.img = self.IMGS[0]


	def draw(self, win):
		self.img = self.IMGS[0]
		win.blit(self.img, (self.x, self.y))

	def move(self):
		self.tick += 1
		disp = self.vel*self.tick + 0.5*GRAVITY*(self.tick**2)

		if disp >= 16:
			disp = (disp/abs(disp)) * 16

		# if disp < 0:
		# 	disp -= 2
			
		self.y += disp


	def jump(self):
		self.vel = VELOCITY_UP
		self.tick = 0

	def get_mask(self):
		return pg.mask.from_surface(self.img)
