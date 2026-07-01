import pygame
from Settings import rgb_type, pos_type, size_type


class Button:
  def __init__(
    self,
    parent: pygame.Surface,
    parent_pos: tuple[int, int],
    pos: pos_type,
    size: size_type,
    action: callable,
    color: rgb_type = (25, 190, 150),
  ):
    self.parent = parent
    self.parent_pos = parent_pos
    self.pos = pos
    self.size = size
    self.color = color
    self.button = pygame.draw.rect(parent, color, pos + size)
    self.action = action

  def on_click(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    relative_x, relative_y = self.parent_pos
    if (
      relative_x < mouse_x < self.parent.get_width()
      and relative_y < mouse_y < self.parent.get_height()
    ):
      self.action()
