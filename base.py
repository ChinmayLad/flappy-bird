from setup import *

class Base:

  def __init__(self):
    self.IMG = GFX['base']
    self.WIDTH = self.IMG.get_width()

    self.x1 = 0
    self.x2 = self.WIDTH

    self.y = FLOOR

  def draw(self, win):
    win.blit(self.IMG, (self.x1, self.y))
    win.blit(self.IMG, (self.x2, self.y))


  def move(self):
    self.x1 -= H_VEL
    self.x2 -= H_VEL

    if self.x1 + self.WIDTH < 0:
      self.x1 = self.x2 + self.WIDTH

    if self.x2 + self.WIDTH < 0:
      self.x2 = self.x1 + self.WIDTH