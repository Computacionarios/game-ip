import pygame
from utils.Button import Button


class ScreenBase:
  def __init__(self, game):
    self.game = game

    self.selectables: list[Button] = [None]
    self.hovering_btn_idx = 0
    self.selected_btn = self.selectables[self.hovering_btn_idx]

  def handle_events(self, events: list[pygame.event.Event]):
    pass

  def update(self):
    pass

  def surf(self, direction):
    if direction == "n":
      self.hovering_btn_idx += 1 if self.hovering_btn_idx < len(self.selectables) - 1 else 0  # fmt: skip
      self.selected_btn = self.selectables[self.hovering_btn_idx]
    elif direction == "p":
      self.hovering_btn_idx -= 1 if self.hovering_btn_idx > 0 else 0
      self.selected_btn = self.selectables[self.hovering_btn_idx]

  def render(self, screen: pygame.Surface):
    pass
