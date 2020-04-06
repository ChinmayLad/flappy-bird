import pygame
import os
import PIL.Image as Image
import numpy
from tools import load_image
pygame.font.init()  # init font

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 700
STAT_FONT = pygame.font.SysFont("Eight\-Bit Madness", 50)
END_FONT = pygame.font.SysFont("Eight\-Bit Madness", 70)
DRAW_LINES = False
GRAVITY = 3
H_VEL = 7
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

GFX = dict()
res_path = 'resources'
GFX['bird'] = [load_image(os.path.join(res_path, "bird{}.png".format(i))) for i in range(1,4)]
GFX['base'] = load_image(os.path.join(res_path, "base.png"))
GFX['pipe'] = load_image(os.path.join(res_path, "pipe.png"))
GFX['bg'] = load_image(os.path.join(res_path, "bg.png"), scale=(WIN_WIDTH,WIN_HEIGHT))