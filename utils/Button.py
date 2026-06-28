import pygame
from game_data import (
  Main_Font,
  BTN_BACKGROUND,
  PRIMARY_DARK,
  SECONDARY,
  SECONDARY_DARK,
  button_border_thickness,
)


class Button:
  def __init__(
    self,
    screen: pygame.Surface,
    text_input: str,
  ):
    self._screen = screen

    self.text_input = text_input
    self.text = Main_Font.render(text_input, True, "white")
    self.is_selected = False

  def render(
    self,
    size: tuple[int, int],
    pos: tuple[int, int],
  ):
    self.size = self.width, self.height = size
    self.pos = self.x, self.y = pos
    self.text_rect = self.text.get_rect(
      center=(self.x + self.width / 2, self.y + self.height / 2 - 1)
    )

    if self.is_selected:
      pygame.draw.rect(
        self._screen,
        SECONDARY,
        (
          self.x - button_border_thickness * 1.5,
          self.y - button_border_thickness * 1.5,
          self.width + button_border_thickness * 3,
          self.height + button_border_thickness * 3,
        ),
      )

      pygame.draw.rect(
        self._screen,
        SECONDARY_DARK,
        (
          self.x + self.width / 2,
          self.y - button_border_thickness,
          self.width / 2 + button_border_thickness,
          self.height + button_border_thickness * 2,
        ),
      )

    self.border = pygame.draw.rect(
      self._screen,
      PRIMARY_DARK,
      (
        self.x - button_border_thickness,
        self.y - button_border_thickness,
        self.width + button_border_thickness * 2,
        self.height + button_border_thickness * 2,
      ),
    )

    self.content = pygame.draw.rect(self._screen, BTN_BACKGROUND, (self.pos, self.size))
    self._screen.blit(self.text, self.text_rect)

  def on_hover(self):
    self.is_selected = True

  def on_release(self):
    self.is_selected = False

  def on_click(self):
    pass
