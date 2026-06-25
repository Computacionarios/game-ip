import os
import sys
import pygame

if __package__ is None and __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from interfaces.Home import Home


class Game:
    def __init__(self):
        pygame.init()
        self._running = True
        self._screen = None
        self.size = self.width, self.height = 800, 600
        self._screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self._running = True
        self.screens = {"home": Home(self)}
        self.curr_screen = self.screens["home"]

    def cleanup(self):
        pygame.quit()

    def change_screen(self, new_screen_name:str):
        self.curr_screen = self.screens[new_screen_name]
    
    def run(self):
        while self._running:
            events = pygame.event.get()
            self.curr_screen.handle_events(events)
            self.curr_screen.render(self._screen)

            pygame.display.flip()
        self.cleanup()
