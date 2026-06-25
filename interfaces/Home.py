import pygame
from .Base_Screen import ScreenBase
from utils.Button import Button
from game_data.colors import background
# from src.game import Game


class Home(ScreenBase):
    def __init__(self, game):
        start_btn_size = (100, 45)
        super().__init__(game)
        self.start_btn = Button(
            game._screen,
            start_btn_size,
            (
                game._screen.width / 2 - start_btn_size[0] / 2 - 20,
                game._screen.height - start_btn_size[1] / 2 - 20,
            ),
            "Começar",
        )

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game._running = False
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game._running = False
                    continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.start_btn.border_rect.collidepoint(mouse_pos):
                    print("teste")

    def render(self, screen: pygame.Surface):
        screen.fill(background)
        self.start_btn.render()
        # self.config_btn.render()
        pygame.draw.line(
            self.game._screen,
            (200, 200, 200),
            (self.game._screen.width / 2, 0),
            (self.game._screen.width / 2, self.game._screen.height),
        )
