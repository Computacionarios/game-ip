import pygame


class _FontLoader:
    def __init__(self, font_name: str, size: int):
        self.font_name = font_name
        self.size = size
        self._font = None

    def _get_font(self):
        if self._font is None:
            self._font = pygame.font.Font(self.font_name, self.size)
        return self._font

    def render(self, *args, **kwargs):
        return self._get_font().render(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self._get_font(), name)


Main_Font = _FontLoader("assets/fonts/main_font.ttf", 24)
