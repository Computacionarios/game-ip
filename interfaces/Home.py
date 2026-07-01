import pygame
from .Base_Screen import ScreenBase
from utils import Button
from game_data import BACKGROUND
from src import iniciar_jogo


class StartButton(Button):
  def on_click(self):
    iniciar_jogo()


class ConfigButton(Button):
  def on_click(self):
    print("config")


class Home(ScreenBase):
  def __init__(self, game):
    super().__init__(game)
    self.start_btn = StartButton(
      game._screen,
      "Começar",
    )

    self.config_btn = ConfigButton(
      game._screen,
      "Configurar",
    )

    self.selectables = [self.start_btn, self.config_btn]
    self.selected_btn = self.selectables[self.hovering_btn_idx]
    self.selected_btn.on_hover()

  def handle_events(self, events):
    for event in events:
      if event.type == pygame.QUIT:
        self.game._running = False
        continue

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.game._running = False
          continue

        if event.key == pygame.K_d:
          self.selected_btn.on_release()
          self.surf("n")
          self.selected_btn.on_hover()

        if event.key == pygame.K_a:
          self.selected_btn.on_release()
          self.surf("p")
          self.selected_btn.on_hover()

        if event.key == pygame.K_SPACE:
          self.selected_btn.on_click()

  def render(self, ):
    self.game._screen.fill(BACKGROUND)
    start_btn_size = start_btn_width, start_btn_height = (90, 40)

    self.start_btn.render(
      start_btn_size,
      (
        self.game._screen.width / 2 - start_btn_width - 20,
        self.game._screen.height - start_btn_height - 50,
      ),
    )

    config_btn_size = config_btn_width, config_btn_height = (110, 40)
    self.config_btn.render(
      config_btn_size,
      (
        self.game._screen.width / 2 + 20,
        self.game._screen.height - config_btn_height - 50,
      ),
    )
    pygame.draw.line(
      self.game._screen, (200, 200, 200), (self.game._screen.width / 2, 0), (self.game._screen.width / 2, self.game._screen.height)
    )
