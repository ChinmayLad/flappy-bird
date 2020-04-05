import pygame
import os

def load_image(path, scale='2x'):
  img = pygame.image.load(path).convert_alpha()
  if scale == '2x':
    img = pygame.transform.scale2x(img)
  else:
    img = pygame.transform.scale(img, scale)
  return img