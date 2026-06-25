import pygame
# from src.game import Game


class ScreenBase:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events: list[pygame.Event]):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        pass
