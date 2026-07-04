import pygame
import sprites
from inventario import Inventario

pygame.init()

inventario = Inventario()


###TELA###
tamanho_tela = (1280, 720)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Aventura Magica")

mapa = pygame.image.load("assets/images/Mapa.png").convert_alpha()
mapa =  pygame.transform.scale(mapa, (7955, 4940))

###PLAYER###
class Player:
    def __init__(self):
        self.x = 1280/2
        self.y = 720-32/2

        self.run_costas, self.run_frente, self.run_esquerda, self.run_direita, self.parado = sprites.movimento_player()

        self.frame = 0
        self.atual_pos = 0
        self.imagem = self.parado[0]

    def update(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
            self.frame += 0.1
            self.x += 10
            self.atual_pos = 1

            if self.frame > len(self.run_esquerda):
                self.frame = 0

            self.imagem = self.run_esquerda[int(self.frame)]

            if personagem.colliderect(barreira):
                self.x -= 11

                

        elif tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
            self.frame += 0.1
            self.x -= 10
            self.atual_pos = 2

            if self.frame > len(self.run_direita):
                self.frame = 0

            self.imagem = self.run_direita[int(self.frame)]

            if personagem.colliderect(barreira):
                self.x += 11

        elif tecla[pygame.K_w] or tecla[pygame.K_UP]:
            self.frame += 0.1
            self.y += 10
            self.atual_pos = 3

            if self.frame > len(self.run_costas):
                self.frame = 0

            self.imagem = self.run_costas[int(self.frame)]

            if personagem.colliderect(barreira):
                self.y -= 11

        elif tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
            self.frame += 0.1
            self.y -= 10
            self.atual_pos = 0

            if self.frame > len(self.run_frente):
                self.frame = 0

            self.imagem = self.run_frente[int(self.frame)]

            if personagem.colliderect(barreira):
                self.y -= 11

        else:
            self.frame = 0
            self.imagem = self.parado[self.atual_pos]

    def draw(self, tela):
        tamanho_sprite = (96, 96)
        personagem = pygame.transform.scale(self.imagem, tamanho_sprite)
        tela.blit(personagem, (1280//2, 720//2))

###Coletavel###

class Coletavel:
    def __init__(self, tipo):
        if tipo == 'cura':
            self.sprite = sprites.coletavel_cura()
        elif tipo == 'mana':
            self.sprite = sprites.coletavel_mana()
        elif tipo == 'imunidade':
            self.sprite = sprites.coletavel_imunidade()
        self.frame = 0
        self.image = self.sprite[0]
        self.coletado = False

    def verificar_colisao(self, jogador):
        if not self.coletado and jogador.colliderect(self.retangulo):
            self.coletado = True
            return True
        return False

    def update_coletavel(self, x, y):
        self.frame += 0.1
        self.x = x
        self.y = y
        self.retangulo = pygame.Rect(x, y, 32, 32)
    
        if self.frame > len(self.sprite):
            self.frame = 0

        self.image = self.sprite[int(self.frame)]

    def draw_coletavel(self, tela):

        if self.coletado:
            return
        
        tamanho_sprite = (32, 32)
        
        carta = pygame.transform.scale(self.image, tamanho_sprite)
        tela.blit(carta, (self.x, self.y))



player = Player()

cura = Coletavel("cura")
cura1 = Coletavel("cura")
cura2 = Coletavel("cura")
cura3 = Coletavel("cura")
cura4 = Coletavel("cura")
cura5 = Coletavel("cura")

mana = Coletavel("mana")
mana1 = Coletavel("mana")
mana2 = Coletavel("mana")
mana3 = Coletavel("mana")
mana4 = Coletavel("mana")
mana5 = Coletavel("mana")

imunidade = Coletavel("imunidade")
imunidade1 = Coletavel("imunidade")
imunidade2 = Coletavel("imunidade")

time = pygame.Clock()

continua = True

inventario.definir_sprites_cartas({
    "cura": pygame.transform.scale(pygame.image.load("assets/images/Cartas/Utilitarios/cura.png").convert_alpha(), (60, 60)),
    "mana": pygame.transform.scale(pygame.image.load("assets/images/Cartas/Utilitarios/bencao.png").convert_alpha(), (60, 60)),
    "imunidade": pygame.transform.scale(pygame.image.load("assets/images/Cartas/Utilitarios/invisibilidade.png").convert_alpha(), (60, 60))
})

carta_selecionada = True
invent = False
while continua:
    ###Camera###
    camera_x = player.x - 7955//2
    camera_y = player.y - 4940//2

    ###BARREIRA###
    barreira = pygame.Rect(camera_x, camera_y + 300, 7955, 300)
    personagem = pygame.Rect(1280//2, 720//2, 96, 96)
    carta = pygame.Rect(1280//2, 720//2, 96, 96)


    time.tick(60)
    tela.blit(mapa, (camera_x, camera_y))

    if not invent:
        player.update()

   
    cura.update_coletavel((542+50)*5 + camera_x, (419+50)*5 + camera_y)
    cura1.update_coletavel((984+50)*5 + camera_x, (603+50)*5 + camera_y)
    cura2.update_coletavel((745+50)*5 + camera_x, (794+50)*5 + camera_y)
    cura3.update_coletavel((568+50)*5 + camera_x, (655+50)*5 + camera_y)
    cura4.update_coletavel((187+50)*5 + camera_x, (384+50)*5 + camera_y)
    cura5.update_coletavel((222+50)*5 + camera_x, (174+50)*5 + camera_y)

    mana.update_coletavel((1142+50)*5 + camera_x, (152+50)*5 + camera_y)
    mana1.update_coletavel((684+50)*5 + camera_x, (258+50)*5 + camera_y)
    mana2.update_coletavel((277+50)*5 + camera_x, (778+50)*5 + camera_y)
    mana3.update_coletavel((245+50)*5 + camera_x, (636+50)*5 + camera_y)
    mana4.update_coletavel((361+50)*5 + camera_x, (123+50)*5 + camera_y)
    mana5.update_coletavel((529+50)*5 + camera_x, (171+50)*5 + camera_y)

    imunidade.update_coletavel((1265+50)*5 + camera_x, (410+50)*5 + camera_y)
    imunidade1.update_coletavel((858+50)*5 + camera_x, (665+50)*5 + camera_y)
    imunidade2.update_coletavel((397+50)*5 + camera_x, (400+50)*5 + camera_y)
    
    if cura.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura.coletado = True

    if not cura1.coletado and personagem.colliderect(cura1.retangulo):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura1.coletado = True

    if not cura2.coletado and personagem.colliderect(cura2.retangulo):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura2.coletado = True

    if not cura3.coletado and personagem.colliderect(cura3.retangulo):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura3.coletado = True

    if not cura4.coletado and personagem.colliderect(cura4.retangulo):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura4.coletado = True

    if not cura5.coletado and personagem.colliderect(cura5.retangulo):
            inventario.adicionar_itens(id = 0, sprite="cura", nome="Carta de Cura")
            cura5.coletado = True


    if mana.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana.coletado = True

    if mana1.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana1.coletado = True

    if mana2.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana2.coletado = True

    if mana3.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana3.coletado = True

    if mana4.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana4.coletado = True

    if mana5.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 1, sprite="mana", nome="Carta de Cura")
            mana5.coletado = True

    if imunidade.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 2, sprite="imunidade", nome="Carta de Cura")
            imunidade.coletado = True

    if imunidade1.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 2, sprite="imunidade", nome="Carta de Cura")
            imunidade1.coletado = True

    if imunidade2.verificar_colisao(personagem):
            inventario.adicionar_itens(id = 2, sprite="imunidade", nome="Carta de Cura")
            imunidade2.coletado = True



    sprite_inventario = pygame.transform.scale(player.imagem, (96, 96))
    inventario.definir_sprite_player(sprite_inventario)

    player.draw(tela)

    if not cura.coletado:
        cura.draw_coletavel(tela)
    if not cura1.coletado:
        cura1.draw_coletavel(tela)
    if not cura2.coletado:
        cura2.draw_coletavel(tela)
    if not cura3.coletado:
        cura3.draw_coletavel(tela)
    if not cura4.coletado:
        cura4.draw_coletavel(tela)
    if not cura5.coletado:
        cura5.draw_coletavel(tela)

    if not mana.coletado:
        mana.draw_coletavel(tela)

    if not mana1.coletado:
        mana1.draw_coletavel(tela)

    if not mana2.coletado:
        mana2.draw_coletavel(tela)

    if not mana3.coletado:
        mana3.draw_coletavel(tela)

    if not mana4.coletado:
        mana4.draw_coletavel(tela)

    if not mana5.coletado:
        mana5.draw_coletavel(tela)    
   
    if not imunidade.coletado:
        imunidade.draw_coletavel(tela)

    if not imunidade1.coletado:
        imunidade1.draw_coletavel(tela)

    if not imunidade2.coletado:
        imunidade2.draw_coletavel(tela)

    if inventario.aberto:
        inventario.desenhar_inventario(tela)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continua = False

        inventario.captura_evento(evento)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_i:
                inventario.abre_fecha_inventario()
                invent = not invent


    pygame.time.wait(1)
    pygame.display.flip()

    
pygame.quit()