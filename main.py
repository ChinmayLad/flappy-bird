import pygame
from setup import *
from bird import Bird
from base import Base
from pipe import Pipe
pygame.font.init()  # init font


def game_over():
	print("GAME OVER LOL!!")

def main():

	bird = Bird(200, 350)
	base = Base()
	pipes = [Pipe(100+WIN_WIDTH)]
	clock = pygame.time.Clock()
	run = True
	score = 0
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
			p.draw(WIN)
		base.draw(WIN)
		bird.draw(WIN)

		base.move()
		bird.move()


		score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
		WIN.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

		rem = []
		add_pipe = False
		for p in pipes:
			p.move()
			if p.collide(bird):
				run = False
				game_over()

			if p.offscreen():
				rem.append(p)

			if not p.passed and p.x < bird.x:
				p.passed = True
				add_pipe = True

		if add_pipe:
			score += 1
			pipes.append(Pipe(100+WIN_WIDTH))
			

		for p in rem:
			pipes.remove(p)

		pygame.display.update()

	main()

main()
