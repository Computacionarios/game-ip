import json
import pygame
from game_settings import TILE_SIZE, TILES_AMOUNT


class World:
  def __init__(self):
    self.load_save()

    self.obstacles: list[pygame.Rect] = []
    self.death_spots: list[pygame.Rect] = []
    self.player_origin = (50,50)

    self.tile_size = TILE_SIZE
    self.tiles_amount = TILES_AMOUNT

    self.screen_size = self.tile_size * self.tiles_amount

    self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

  def load_save(self):
    try:
      with open("C:/Users/mvhx/Documents/game-ip/data/cache.json") as world:
        self.map = json.load(world)

      with open("C:/Users/mvhx/Documents/game-ip/data/settings.json") as settings:
        self.settings = json.load(settings)
    except FileNotFoundError:
      print("Mapa não encontrado")

  def draw(self):
    for y_idx, line in enumerate(self.map):
      for x_idx, tile_id in enumerate(line):
        x = self.tile_size * x_idx
        y = self.tile_size * y_idx

        colors = self.settings["pallet_colors"]
        colors_names = tuple(colors.keys())

        tile = pygame.draw.rect(
          self.screen,
          colors[colors_names[tile_id]] if tile_id >= 0 else (50,50,50),
          (x, y, self.tile_size, self.tile_size),
        )
        if colors_names[tile_id] == "black":
          self.obstacles.append(tile)

        if colors_names[tile_id] == "red":
          self.death_spots.append(tile)

        if colors_names[tile_id] == "blue":
          self.player_origin = (x, y)
