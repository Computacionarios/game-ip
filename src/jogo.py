import pygame
import sprites as sprite

pygame.init()

###TELA###
tamanho_tela = pygame.display.get_desktop_sizes()
# tamanho_tela[0] -= 40
tela = pygame.display.set_mode(tamanho_tela[0])
pygame.display.set_caption("Aventura Magica")

mapa = pygame.image.load("assets/images/Mapa.png").convert_alpha()
mapa = pygame.transform.scale(mapa, (7955, 4940))


###PLAYER###
class Player:
  def __init__(self):
    self.x = 1280 / 2
    self.y = 720 - 32 / 2

    (
      self.run_costas,
      self.run_frente,
      self.run_esquerda,
      self.run_direita,
      self.parado,
    ) = sprite.movimento_player()

    self.frame = 0
    self.atual_pos = 0
    self.imagem = self.parado[0]

  def update(self):
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
      self.frame += 0.1
      self.x += 3
      self.atual_pos = 1

      if self.frame > len(self.run_esquerda):
        self.frame = 0

      self.imagem = self.run_esquerda[int(self.frame)]

      if personagem.colliderect(barreira):
        self.x -= 3

    elif tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
      self.frame += 0.1
      self.x -= 3
      self.atual_pos = 2

      if self.frame > len(self.run_direita):
        self.frame = 0

      self.imagem = self.run_direita[int(self.frame)]

      if personagem.colliderect(barreira):
        self.x += 3

    elif tecla[pygame.K_w] or tecla[pygame.K_UP]:
      self.frame += 0.1
      self.y += 3
      self.atual_pos = 3

      if self.frame > len(self.run_costas):
        self.frame = 0

      self.imagem = self.run_costas[int(self.frame)]

      if personagem.colliderect(barreira):
        self.y -= 3

    elif tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
      self.frame += 0.1
      self.y -= 3
      self.atual_pos = 0

      if self.frame > len(self.run_frente):
        self.frame = 0

      self.imagem = self.run_frente[int(self.frame)]

      if personagem.colliderect(barreira):
        self.y -= 3

    else:
      self.frame = 0
      self.imagem = self.parado[self.atual_pos]

  def draw(self, tela):
    tamanho_sprite = (96, 96)
    personagem = pygame.transform.scale(self.imagem, tamanho_sprite)
    tela.blit(personagem, (1280 // 2, 720 // 2))


###Coletavel###
coletavel_forma = sprite.coletavel_forma()

coletavel_elemental = sprite.coletavel_elemento()

coletavel_utilitario = sprite.coletavel_utilitario()
player = Player()

time = pygame.Clock()

continua = True
frame1 = 0
frame2 = 0
frame3 = 0

while continua:
  ###Camera###
  camera_x = player.x - 7955 // 2
  camera_y = player.y - 4940 // 2

  ###BARREIRA###
  barreira = pygame.Rect(camera_x, camera_y + 300, 7955, 300)
  personagem = pygame.Rect(1280 // 2, 720 // 2, 96, 96)

  time.tick(60)
  tela.blit(mapa, (camera_x, camera_y))

  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      continua = False

  player.update()

  player.draw(tela)

  frame1 += 0.1
  frame2 += 0.1
  frame3 += 0.1

  if frame1 > len(coletavel_forma):
    frame1 = 0
  if frame2 > len(coletavel_elemental):
    frame2 = 0
  if frame3 > len(coletavel_utilitario):
    frame3 = 0

  imagem1 = coletavel_forma[int(frame1)]
  imagem2 = coletavel_elemental[int(frame2)]
  imagem3 = coletavel_utilitario[int(frame3)]

  tamanho_sprite = (64, 64)

  carta1 = pygame.transform.scale(imagem1, tamanho_sprite)
  tela.blit(carta1, (1000 + camera_x, 2000 + camera_y))

  carta2 = pygame.transform.scale(imagem2, tamanho_sprite)
  tela.blit(carta2, (2000 + camera_x, 1000 + camera_y))

  carta3 = pygame.transform.scale(imagem3, tamanho_sprite)
  tela.blit(carta3, (3000 + camera_x, 2000 + camera_y))

  pygame.time.wait(1)
  pygame.display.flip()

pygame.quit()
