from setup import *
import random

class Pipe:

  def __init__(self, x):
    self.BOTTOM = GFX['pipe']
    self.TOP = pygame.transform.flip(self.BOTTOM, False, True)
    self.WIDTH = self.BOTTOM.get_width()
    self.HEIGHT = self.BOTTOM.get_height()
    self.GAP = 200

    self.passed = False

    self.x = x

    self.bottom = random.randint(250, WIN_HEIGHT-300)
    self.top = self.bottom-self.GAP-self.HEIGHT


  def draw(self, win):
    win.blit(self.BOTTOM, (self.x, self.bottom))
    win.blit(self.TOP, (self.x,  self.top))


  def move(self):
    self.x -= H_VEL

  def offscreen(self):
    return self.x+self.WIDTH < 0

  def collide(self, bird):
    bird_mask, w, h = bird.get_mask()
    top_mask = pygame.mask.from_surface(self.TOP)
    bottom_mask = pygame.mask.from_surface(self.BOTTOM)

    top_offset = (self.x - bird.x, self.top - round(bird.y))
    bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

    top_overlap = bird_mask.overlap(top_mask, top_offset)
    bottom_overlap = bird_mask.overlap(bottom_mask, bottom_offset)

    return top_overlap or bottom_overlap

  def get_top(self):
    return self.top + self.HEIGHT

  def get_bottom(self):
    return self.bottom
