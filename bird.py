from setup import *
import pygame as pg

ANIMATION = 5
VELOCITY_UP = -10.5
MAX_ROTATION = 20
ROT_VEL = 10
class Bird:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.vel = 0
    self.tick = 0
    self.tilt = 0
    self.img_count = 0
    self.height = self.y
    self.IMGS = GFX['bird']
    self.img = self.IMGS[0]


  def draw(self, win):
    self.img_count += 1

    if self.img_count <= ANIMATION:
      self.img = self.IMGS[0]
    elif self.img_count <= ANIMATION*2:
      self.img = self.IMGS[1]
    elif self.img_count <= ANIMATION*3:
      self.img = self.IMGS[2]
    elif self.img_count <= ANIMATION*4:
      self.img = self.IMGS[1]
    elif self.img_count <= ANIMATION*4 +1:
      self.img = self.IMGS[0]
      self.img_count = 0

    if self.tilt <= -80:
      self.img = self.IMGS[1]
      self.img_count = ANIMATION*2

    self.rotateCenter(win)

  def move(self):
    self.tick += 1
    disp = self.vel*self.tick + 0.5*GRAVITY*(self.tick**2)

    if disp >= 17:
      disp = (disp/abs(disp)) * 17

    if disp < 0:
      disp -= 2
      
    self.y += disp

    if disp < 0 and self.y < self.height:
      if self.tilt <= MAX_ROTATION:
        self.tilt += MAX_ROTATION
    else:
      if self.tilt >= -90:
        self.tilt -= ROT_VEL


  def jump(self):
    self.vel = VELOCITY_UP
    self.tick = 0
    self.height = self.y

  def get_mask(self):
    return pg.mask.from_surface(self.img), self.img.get_width(), self.img.get_width()


  def rotateCenter(self, win):
    new_image = pg.transform.rotate(self.img, self.tilt)
    new_rect = new_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
    win.blit(new_image, new_rect)