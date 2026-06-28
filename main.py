import pygame
from interfaces.Home import Home


class Main:
  def __init__(self):
    pygame.init()
    self._running = True
    self.is_fullscreen = False
    size = (800, 600)
    self._screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    self._running = True
    self.screens = {
      "home": Home(self),
    }
    self.curr_screen = self.screens["home"]

  def cleanup(self):
    pygame.quit()

  def resize(self):
    self.is_fullscreen = not self.is_fullscreen
    size = pygame.display.get_desktop_sizes()[0] if self.is_fullscreen else (800, 600)
    self._screen = pygame.display.set_mode(
      size,
      pygame.FULLSCREEN | pygame.SCALED if self.is_fullscreen else pygame.RESIZABLE,
    )

  def change_screen(self, new_screen_name: str):
    self.curr_screen = self.screens[new_screen_name]

  def run(self):
    while self._running:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_f:
            self.resize()
      self.curr_screen.handle_events(events)
      self.curr_screen.render()

      pygame.display.flip()
    self.cleanup()


if __name__ == "__main__":
  Main().run()
