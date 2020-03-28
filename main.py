import pygame
from setup import *
from bird import Bird
from base import Base
from pipe import Pipe
pygame.font.init()  # init font


def game_over():
	print("GAME OVER LOL!!")

def main():
	# global WIN
	# win = WIN1


	bird = Bird(200, 350)
	base = Base()
	pipes = [Pipe(100+WIN_WIDTH)]
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				quit()
				break
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird.jump()


		WIN.blit(GFX['bg'], (0,0))

		for p in pipes:
			p.move()
			p.draw(WIN)
		base.move()
		bird.move()
		base.draw(WIN)
		bird.draw(WIN)

		for p in pipes:
			if p.collide(bird):
				run = False
				game_over()

		if pipes[-1].crossed(bird):
			pipes.append(Pipe(100+WIN_WIDTH))
			

		if pipes[0].offscreen():
			pipes.pop(0)

		pygame.display.update()

	main()

main()
