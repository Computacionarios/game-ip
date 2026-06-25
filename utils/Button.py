import pygame
from game_data import Main_Font, primary_dark, secondary, button_border_thickness


class Button:
    def __init__(
        self,
        screen: pygame.Surface,
        size: tuple[int, int],
        pos: tuple[int, int],
        text_input: str,
    ):
        self.screen = screen
        self.size = self.width, self.height = size
        self.pos = self.x, self.y = pos

        container_pos = (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2)

        self.content_rect = pygame.Rect(container_pos, self.size)
        self.border_rect = pygame.Rect(
            container_pos[0] - button_border_thickness,
            container_pos[1] - button_border_thickness,
            self.width + button_border_thickness * 2,
            self.height + button_border_thickness * 2,
        )

        self.text_input = text_input
        self.text = Main_Font.render(text_input, True, "white")
        self.text_rect = self.text.get_rect(center=self.pos)

    def render(self):
        self.border = pygame.draw.rect(self.screen, primary_dark, self.border_rect)
        self.content = pygame.draw.rect(self.screen, secondary, self.content_rect)
        self.screen.blit(self.text, self.text_rect)

    def on_hover(self):
        self.text = Main_Font.render(self.text_input, True, "red")

    def on_release(self):
        self.text = Main_Font.render(self.text_input, True, "red")

    def on_click(self, do_something):
        do_something()
