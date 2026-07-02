import pygame
import pygame.locals as pg_lc

from Settings import CANVAS_SIZE, PALLET_WIDTH, BORDER
from src.Canvas import Canvas
from src.Pallet import Pallet

pygame.init()
pygame.display.set_caption("Map Maker")

screen = pygame.display.set_mode(
  (CANVAS_SIZE[0] + PALLET_WIDTH + BORDER * 3, CANVAS_SIZE[1] + BORDER * 2),
  pygame.RESIZABLE,
)

pallet = Pallet(screen.width - PALLET_WIDTH - BORDER)
canvas = Canvas(screen)
pallet.draw_pallet(screen)

running_game = True
while running_game:
  for event in pygame.event.get():
    if event.type == pg_lc.QUIT:
      canvas.save_map()
      running_game = False
      continue

    if pygame.key.get_pressed()[pg_lc.K_ESCAPE]:
      canvas.save_map()
      running_game = False
      continue

  if pygame.mouse.get_pressed()[0]:
    pallet.change_color()
    canvas.draw(pallet.selected_color)

  if pygame.mouse.get_pressed()[1]:
    canvas.clean_all()

  if pygame.mouse.get_pressed()[2]:
    canvas.draw(-1)

  pygame.display.update()

pygame.quit()
