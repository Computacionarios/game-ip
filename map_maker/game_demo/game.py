import pygame
from game_settings import TILE_SIZE
from src.Player import Player
from src.World import World

from game_settings import JUMP_HEIGHT, CHARACTER_MOVE


world = World()
world.draw()
screen_width = world.screen_size
screen_height = world.screen_size

timer = pygame.time.Clock()

player_origin_x = world.player_origin[0] + TILE_SIZE / 2
player_origin_y = world.player_origin[1] - TILE_SIZE / 3

player = Player(world, player_origin_x, player_origin_y, 2, CHARACTER_MOVE, JUMP_HEIGHT)

running = True
while running:
  timer.tick(40)
  world.screen.fill((25, 25, 25))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        print(world.obstacles[0])
        running = False

  if pygame.key.get_pressed()[pygame.K_d]:
    player.walk("r")

  if pygame.key.get_pressed()[pygame.K_a]:
    player.walk("l")

  if pygame.key.get_pressed()[pygame.K_w]:
    player.walk("u")

  if pygame.key.get_pressed()[pygame.K_s]:
    player.walk("d")

  world.draw()
  player.draw(world.screen)
  pygame.display.update()

pygame.quit()
