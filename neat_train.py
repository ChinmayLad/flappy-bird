import pygame
import neat
from setup import *
from bird import Bird
from base import Base
from pipe import Pipe
pygame.font.init()  # init font

gen = 0

def game_over():
  print("GAME OVER LOL!!")

def eval_genome(genomes, config):
  global gen

  birds = []
  gen += 1
  for _, g in genomes:
    g.fitness = 0
    net = neat.nn.FeedForwardNetwork.create(g, config)
    birds.append(Bird(200, 350, g, net))

  base = Base()
  pipes = [Pipe(100+WIN_WIDTH)]
  clock = pygame.time.Clock()
  run = True
  score = 0

  while run and len(birds) > 0:
    clock.tick(30)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        quit()
        break

    pipe_ind = 0
    if len(pipes)>0 and birds[0].x > pipes[0].x + pipes[0].WIDTH:
      pipe_ind = 1

    for i, bird in enumerate(birds):
      bird.gene.fitness += 0.1
      out = bird.net.activate((bird.y, abs(bird.y - pipes[pipe_ind].get_top()), abs(bird.y - pipes[pipe_ind].get_bottom())))
      if out[0] > 0.5:
        bird.jump()

    WIN.blit(GFX['bg'], (0,0))

    for p in pipes:
      p.draw(WIN)

    base.draw(WIN)
    base.move()
    for bird in birds:
      bird.draw(WIN)
      bird.move()

    rem = []
    bird_rem = []
    add_pipe = False
    for p in pipes:
      p.move()
      for bird in birds:
        if p.collide(bird):
          bird_rem.append(bird)
          continue

        if not p.passed and p.x < bird.x:
          bird.gene.fitness += 5
          p.passed = True
          add_pipe = True

      if p.offscreen():
          rem.append(p)

    for bird in bird_rem:
      bird.gene.fitness -= 1
      birds.remove(bird)

    if add_pipe:
      score += 1
      pipes.append(Pipe(100+WIN_WIDTH))

    for p in rem:
      pipes.remove(p)

    for bird in birds:
      if bird.y > WIN_HEIGHT + 10:
        birds.pop(birds.index(bird))


    score_label = STAT_FONT.render("Score: {}".format(score), 1, (255,255,255))
    WIN.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    gen_label = STAT_FONT.render("Gen: {}".format(gen), 1, (255,255,255))
    WIN.blit(gen_label, (15, 10))

    birds_label = STAT_FONT.render("Birds: {}".format(len(birds)), 1, (255,255,255))
    WIN.blit(birds_label, (10, gen_label.get_height() + 5))

    if score > 20:
      break
      
    # pygame.image.save(WIN, "images/flappy-gen{}-counter{}.png".format(gen, pygame.time.get_ticks()))
    pygame.display.update()





def run(config_file):
  global gen
  gen = 0
  config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
    neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)

  p = neat.Population(config)

  p.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  p.add_reporter(stats)
  p.add_reporter(neat.Checkpointer(5))

  winner = p.run(eval_genome, 20)

  print('\nBest genome:\n{!s}'.format(winner))

  # # Show output of the most fit genome against training data.
  # print('\nOutput:')





if __name__ == "__main__":
  local_dir = os.path.dirname(__file__)
  config_path = os.path.join(local_dir, 'neat_config.txt')
  run(config_path)