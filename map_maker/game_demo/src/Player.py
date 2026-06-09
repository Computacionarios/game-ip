import pygame
from game_settings import GRAVITY


class Player(pygame.sprite.Sprite):
  def __init__(
    self,
    parent: pygame.Surface,
    x: int,
    y: int,
    scale: int,
    speed: int,
    jump_height: int,
  ):
    self.parent = parent
    self.direction = "l"
    self.flip = False

    img = pygame.image.load("game_demo/assets/imgs/player/0.png")
    self.sprit = pygame.transform.scale(img, (img.width * scale, img.height * scale))
    self.rect = self.sprit.get_rect()
    self.rect.center = (x, y)

    self.speed_x = speed
    self.speed_y = speed

    self.jumping = False
    self.jump_height = jump_height

  def draw(self, parent: pygame.Surface):
    parent.blit(pygame.transform.flip(self.sprit, self.flip, False), self.rect)

  def walk(self, direction: str):
    self.direction = direction
    if direction == "l":
      self.flip = True
    elif direction == "r":
      self.flip = False

    dx = 0
    dy = 0

    match direction:
      case "l":
        dx = -self.speed_x
      case "r":
        dx = self.speed_x
      case "u":
        dy = -self.speed_y
      case "d":
        dy = self.speed_y

    if not (0 < self.rect.x + dx < self.parent.screen.get_width() - self.rect.width):
      return

    if not (0 < self.rect.y + dy < self.parent.screen.get_height() - self.rect.height):
      return

    for tile in self.parent.obstacles:
      if tile.colliderect(
        self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height
      ):
        if direction == "l":
          dx = self.rect.left - tile.right
        if direction == "r":
          dx = tile.left - self.rect.right
        print(dx)
      if tile.colliderect(
        self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height
      ):
        dy = 0

    self.rect.x += dx
    self.rect.y += dy

    for tile in self.parent.death_spots:
      if tile.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
        self.rect.x = self.parent.player_origin[0]
        self.rect.y = self.parent.player_origin[1] - (self.sprit.height / 2)

  def jump(self):
    if not self.jumping:
      self.speed_y = self.jump_height
      self.jumping = True

  def apply_gravity(self):
    self.speed_y += GRAVITY
    self.rect.y += self.speed_y

  def verify_ground(self, ground_y):
    if self.rect.bottom >= ground_y:
      self.rect.bottom = ground_y
      self.jumping = False
      self.speed_y = 0

  def update(self, ground_y):
    self.apply_gravity()
    self.verify_ground(ground_y)
