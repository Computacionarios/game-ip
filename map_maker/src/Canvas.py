import json
import pygame
from Settings import (
  screen_colors,
  pallet_colors,
  BORDER,
  CANVAS_SIZE,
  TILE_SIZE,
)


class Canvas:
  def __init__(self, screen: pygame.Surface):

    self.object_position_list: list[tuple[int, pygame.Rect]] = []  # matrix da tela

    self.saveless_grid: list[int] = []
    self.colors = tuple(pallet_colors.keys())

    self.canvas = screen

    # tamanho da tela, calculada pela relação dos tijolos bordas e gaps
    self.tiles_amount_x = int(CANVAS_SIZE[0] / TILE_SIZE)
    self.tiles_amount_y = int(CANVAS_SIZE[1] / TILE_SIZE)

    map = pygame.image.load("map_maker/src/Mapa.png").convert_alpha()
    self.map = pygame.transform.scale(
      map, (CANVAS_SIZE[0] - BORDER * 2, CANVAS_SIZE[1] - BORDER * 2)
    )

    self.create_grid()
    self.draw_grid()
    self.load_save()

  def save_map(self):
    with open("data/settings.json", "w") as data:
      settings = {
        "tile_size": TILE_SIZE,
        "tiles_amount": (self.tiles_amount_x, self.tiles_amount_y),
        "pallet_colors": pallet_colors,
      }
      json.dump(settings, data, indent=2)

    with open("data/cache.json", "w") as cache:
      json.dump(self.object_position_list, cache, indent=2)

  def load_save(self):
    try:
      with open("data/cache.json") as data:
        cache = json.load(data)

        if len(cache) > 0:
          self.object_position_list = cache
          self.last_len = len(self.object_position_list)
          screen_w_range = range(CANVAS_SIZE[0])
          screen_h_range = range(CANVAS_SIZE[1])

          for slot in self.object_position_list:
            rect = pygame.Rect(slot[1])

            if (rect.x in screen_w_range and rect.width in screen_w_range) and (
              rect.y in screen_h_range and rect.height in screen_h_range
            ):
              pygame.draw.rect(self.canvas, pallet_colors[self.colors[slot[0]]], rect)

    except FileNotFoundError:
      print("Arquivo não encontrado")

  def create_grid(self):  # cria a matriz da tela
    for _ in range(int(self.tiles_amount_y)):
      new_line = []
      for _ in range(int(self.tiles_amount_x)):
        new_line.append([-1])
      self.saveless_grid.append(new_line)

  def draw_grid(self):
    for l_idx, line in enumerate(self.saveless_grid):
      for c_idx, tile in enumerate(line):
        tile_x = TILE_SIZE * c_idx
        tile_y = TILE_SIZE * l_idx

        rect = pygame.draw.rect(
          self.canvas,
          screen_colors["tile_color"],
          (BORDER + tile_x, BORDER + tile_y, TILE_SIZE, TILE_SIZE),
        )

        self.saveless_grid[l_idx][c_idx].append(
          [rect.x, rect.y, rect.width, rect.height]
        )
    self.canvas.blit(self.map, (BORDER, BORDER))

  def draw(self, color_idx: int = None):
    mouse_pos = pygame.mouse.get_pos()
    for l_idx, line in enumerate(self.saveless_grid):
      for c_idx, col in enumerate(line):
        if pygame.Rect(tuple(col[1])).collidepoint(mouse_pos):
          clicked_slot = self.saveless_grid[l_idx][c_idx]

          if color_idx < 0:
            print(clicked_slot)
            if clicked_slot in self.object_position_list:
              idx = self.object_position_list.index(clicked_slot)
              self.object_position_list.pop(idx)
              print("apagado")

          else:
            clicked_slot[0] = color_idx
            if clicked_slot not in self.object_position_list:
              self.object_position_list.append(clicked_slot)
    self.update()

  def clean_all(self):
    self.object_position_list = []
    self.saveless_grid = []
    self.create_grid()
    self.draw_grid()

  def update(self):
    self.canvas.blit(self.map, (BORDER, BORDER))
    for slot in self.object_position_list:
      if slot[0] >= 0:
        pygame.draw.rect(
          self.canvas,
          pallet_colors[self.colors[slot[0]]],
          slot[1],
        )
