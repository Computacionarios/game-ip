import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
container = pygame.Surface((WIDTH, HEIGHT))
zoom_level = 1.0

# Camera state
zoom_level = 1.0
min_zoom = 0.2
max_zoom = 5.0
zoom_speed = 1.1

# Position of the top-left of the camera view in world space
camera_x = 0.0
camera_y = 0.0

# Generate a list of static world objects (rectangles) to display
world_rects = [
  pygame.Rect(100, 100, 50, 50),
  pygame.Rect(300, 200, 100, 80),
  pygame.Rect(500, 400, 60, 60),
  pygame.Rect(200, 450, 80, 50),
]

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check for scroll wheel inputs
      if event.button in (4, 5):  # 4: Scroll Up, 5: Scroll Down
        mouse_x, mouse_y = event.pos

        # 1. Calculate mouse position in world space before zooming
        world_mouse_x = (mouse_x / zoom_level) + camera_x
        world_mouse_y = (mouse_y / zoom_level) + camera_y

        # 2. Update the zoom level factor
        if event.button == 4:  # Zoom In
          zoom_level = min(zoom_level * zoom_speed, max_zoom)
        elif event.button == 5:  # Zoom Out
          zoom_level = max(zoom_level / zoom_speed, min_zoom)

        # 3. Adjust camera position so world mouse aligns with screen mouse
        camera_x = world_mouse_x - (mouse_x / zoom_level)
        camera_y = world_mouse_y - (mouse_y / zoom_level)

  # Drawing phase
  screen.fill((30, 30, 30))

  # Render world objects based on camera offset and zoom scale
  for rect in world_rects:
    pygame.draw.rect(screen, (0, 200, 100), rect)

  pygame.display.flip()
  clock.tick(60)
