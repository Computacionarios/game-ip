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

        sprites_jogador = sprite.Player()

        self.direcao = sprite.FRENTE
        self.sprites_andando = sprites_jogador.andando(self.direcao)
        self.sprites_parado = sprites_jogador.parado(self.direcao)

        self.frame = 0
        self.sprites_atuais = self.sprites_parado

        self.imagem = self.sprites_atuais[int(self.frame)]

        self.delta_v = 5

    def eventos(self):

        tecla = pygame.key.get_pressed()

        self.sprites_atuais = self.sprites_andando
        if self.frame >= len(self.sprites_atuais) - 1:
            self.frame = 0

        if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
            self.frame += 0.1
            self.direcao = sprite.ESQUERDA

            if self.x + self.delta_v >= barreira.left:
                self.x += self.delta_v

        elif tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
            self.frame += 0.1
            self.direcao = sprite.DIREITA

            if self.x - self.delta_v <= barreira.right:
                self.x -= self.delta_v

        elif tecla[pygame.K_w] or tecla[pygame.K_UP]:
            self.frame += 0.1
            self.direcao = sprite.DIREITA

            if self.y + self.delta_v >= barreira.top:
                self.y += self.delta_v

        elif tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
            self.frame += 0.1
            self.direcao = sprite.DIREITA

            if self.y - self.delta_v <= barreira.bottom:
                self.y -= self.delta_v
        else:
            self.frame = 0
            self.sprites_atuais = self.sprites_parado

    def update(self):
        tamanho_sprite = (96, 96)
        sprites_jogador = sprite.Player()
        self.sprites_andando = sprites_jogador.andando(self.direcao)
        self.sprites_parado = sprites_jogador.parado(self.direcao)
        self.imagem = self.sprites_atuais[int(self.frame)]
        self.imagem = pygame.transform.scale(self.imagem, tamanho_sprite)

    def render(self, tela: pygame.Surface):
        tela.blit(self.imagem, (tamanho_tela[0][0] // 2, tamanho_tela[0][1] // 2))


###Coletavel###


class Coletavel:
    def __init__(self, tipo: str, pos: tuple[int, int]):
        self.pos = self.x, self.y = pos
        self.size = self.w, self.h = (40, 40)
        self.ret = pygame.Rect(self.x, self.y, 32, 32)

        sprites_coletaveis = sprite.Coletavel()
        if tipo == "util":
            self.sprites = sprites_coletaveis.util()
        elif tipo == "forma":
            self.sprites = sprites_coletaveis.forma()
        elif tipo == "elemento":
            self.sprites = sprites_coletaveis.elemento()

        self.frame = 0
        self.imagem = self.sprites[0]

    def update(self):
        self.frame += 0.1

        if self.frame > len(self.sprites) - 1:
            self.frame = 0

        self.imagem = self.sprites[int(self.frame)]

    def render(self, tela):
        tamanho_sprite = (32, 32)

        self.imagem = pygame.transform.scale(self.imagem, tamanho_sprite)
        tela.blit(self.imagem, (self.x, self.y))


player = Player()

forma = Coletavel("forma", (300, 100))
elemento = Coletavel("elemento", (300, 100))
util = Coletavel("util", (300, 100))

tempo = pygame.Clock()
rodando = True
while rodando:
    ###Camera###
    camera_x = player.x - 7955 // 2
    camera_y = player.y - 4940 // 2

    ###BARREIRA###
    barreira = pygame.Rect(camera_x, camera_y, 7955, 300)
    personagem = pygame.Rect(1280 // 2, 720 // 2, 96, 96)

    tempo.tick(60)
    tela.blit(mapa, (camera_x, camera_y))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    player.eventos()
    player.update()
    player.render(tela)

    pygame.display.flip()

pygame.quit()
