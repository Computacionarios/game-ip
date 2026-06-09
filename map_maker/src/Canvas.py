import json
import pygame
from Settings import screen_colors, pallet_colors, CANVAS_GAP, BORDER
from game_demo.game_settings import TILE_SIZE, TILES_AMOUNT


class Canvas:
  def __init__(self):
    self.drawings: list = []  # matrix da tela
    self.colors = tuple(pallet_colors.keys())

    self.BORDER = BORDER
    self.gap = CANVAS_GAP  # espaço entre tijolos da tela
    self.tile_size = TILE_SIZE  # tamanho dos tijolos da tela
    self.tiles_amount = TILES_AMOUNT  # numero de tijolos² na tela

    # tamanho da tela, calculada pela relação dos tijolos bordas e gaps
    self.size = (
      self.tile_size * self.tiles_amount
      + self.BORDER * 2
      + self.gap * (self.tiles_amount - 1)
    )
    if not self.load_save():
      self.create_grid()

  def save_game(self):
    with open("game_demo/data/settings.json", "w") as data:
      settings = {
        "tile_size": self.tile_size,
        "tiles_amount": self.tiles_amount,
        "pallet_colors": pallet_colors,
      }
      json.dump(settings, data, indent=2)

    with open("game_demo/data/cache.json", "w") as cache:
      json.dump(self.drawings, cache, indent=2)

  def load_save(self):
    try:
      with open("game_demo/data/cache.json") as data:
        cache = json.load(data)

        if len(cache) > 0:
          self.drawings = cache

          if len(self.drawings) < TILES_AMOUNT:
            for line in self.drawings:
              for _ in range(TILES_AMOUNT - len(line)):
                line.append(-1)

            for _ in range(TILES_AMOUNT - len(self.drawings)):
              self.drawings.append([-1] * TILES_AMOUNT)

          elif len(self.drawings) > TILES_AMOUNT:
            for line in self.drawings:
              for _ in range(len(self.drawings) - TILES_AMOUNT):
                line.pop()

            for _ in range(len(self.drawings) - TILES_AMOUNT):
              self.drawings.pop()
          return True

        return False
    except FileNotFoundError:
      print("Arquivo não encontrado")
      return False

  def create_grid(self):  # cria a matriz da tela
    for _ in range(self.tiles_amount):
      self.drawings.append([-1] * self.tiles_amount)

  def draw_grid(self, screen: pygame.Surface):
    canvas_container = pygame.Rect((0, 0, self.size, self.size))
    self.canvas = screen.subsurface(canvas_container)

    for l_idx, line in enumerate(self.drawings):
      for c_idx, tile in enumerate(line):
        tile_x = (self.gap * c_idx) + self.tile_size * c_idx
        tile_y = (self.gap * l_idx) + self.tile_size * l_idx

        pygame.draw.rect(
          self.canvas,
          screen_colors["tile_color"] if tile < 0 else pallet_colors[self.colors[tile]],
          (BORDER + self.gap + tile_x, BORDER + tile_y, self.tile_size, self.tile_size),
        )

  # desenha na tela com cores especificas ou cores selecionadas da paleta
  def draw(self, color_idx: int = None):
    # o coeficiente de proporção entre um tijolo e outro em relação a matrix
    # se o coeficiente é 2, e o cursor estiver em uma posição entre 1 e 2.9, o indice é 0
    # caso o cursor esteja entre 3 e 4.9, o indice é 1
    mouse_pos = pygame.mouse.get_pos()
    proportion_coef = self.size / self.tiles_amount
    col = int(mouse_pos[0] / proportion_coef)
    line = int(mouse_pos[1] / proportion_coef)

    # caso o mouse esteja nas delimitações da tela e selecione um tijolo registrado
    x_in_range = 0 <= col <= self.tiles_amount - 1
    y_in_range = 0 <= line <= self.tiles_amount - 1
    if x_in_range and y_in_range:
      # desenha nesse tijolo especifico com a cor selecionada
      self.drawings[line][col] = color_idx

  def clean_all(self, screen: pygame.Surface):
    self.drawings = []
    self.create_grid()
    self.draw_grid(screen)
