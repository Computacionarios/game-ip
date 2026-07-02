# arquivo jogador modificado para a biblioteca pygame - teste

import pygame

from inventario import Inventario
import sprites

inventario = Inventario()

sprite_carta = {
    "cura": pygame.image.load("game-ip/assets/images/Cartas/Utilitarios/cura.png").convert_alpha(),
    "mana": pygame.image.load("game-ip/assets/images/Cartas/Utilitarios/bencao.png").convert_alpha(),
    "imunidade": pygame.image.load("game-ip/assets/images/Cartas/Utilitarios/invisibilidade.png").convert_alpha()
}

sprite_player = pygame.image.load("game-ip/assets/images/Player/parado_frente.png").convert_alpha()

inventario.definir_sprite_player(sprite_player)
inventario.definir_sprites_cartas(sprite_carta)



class Personagem(pygame.sprite.Sprite): 
    HP_MAX      = 200
    MP_MAX      = 8 
    SPEED_BASE  = 50

    def __init__(self, nome, x, y): 
        super().__init__() 
        
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 128, 255)) 
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y) 
        
        self.nome         = nome
        self.hp           = self.HP_MAX
        self.mp           = 4 
        self.speed        = self.SPEED_BASE
        self.defesa_atual = 0
        
        self.paralisia = 0
        self.envenenamento = 0
        self.lentidao = 0
        self.imune_paralisia = 0
        self.imune_envenenamento = 0

    @property 
    def vivo(self):  
        return self.hp > 0

    @property
    def hp_pct(self): 
        return self.hp / self.HP_MAX

    @property
    def mp_pct(self): 
        return self.mp / self.MP_MAX

    def receber_dano(self, dano): 
        self.hp = max(0, self.hp - dano)

    def curar(self, valor): 
        antes = self.hp
        self.hp = min(self.HP_MAX, self.hp + valor)
        return self.hp - antes
        
    def recuperar_mp(self, valor):
        self.mp = min(self.MP_MAX, self.mp + valor)

    def processar_efeitos(self): 
        msgs = []
        
        if self.envenenamento > 0:
            dano = 5
            self.receber_dano(dano)
            msgs.append(f"☠️ {self.nome} sofreu {dano} de dano por envenenamento!")
            self.envenenamento -= 1
            
            
        if self.lentidao > 0: self.lentidao -= 1
        if self.imune_paralisia > 0: self.imune_paralisia -= 1
        if self.imune_envenenamento > 0: self.imune_envenenamento -= 1
            
        return msgs

    def status_str(self): 
        status = []
        if self.paralisia > 0: status.append(f"Paralisado({self.paralisia})")
        if self.envenenamento > 0: status.append(f"Envenenado({self.envenenamento})")
        if self.lentidao > 0: status.append(f"Lento({self.lentidao})")
        if self.imune_paralisia > 0: status.append(f"ImuneRaio({self.imune_paralisia})")
        if self.imune_envenenamento > 0: status.append(f"ImuneMetal({self.imune_envenenamento})")
        return ", ".join(status) if status else "—" 

    def update(self):
        if not self.vivo:
            self.image.fill((100, 100, 100)) 

def desenhar_personagem(tela, personagem, fonte_status):
    # Desenha o personagem
    tela.blit(personagem.image, personagem.rect)
    
    # Pega a altura real da fonte para calcular um espaçamento perfeito
    altura_fonte = fonte_status.get_height()
    
    # Nome (Fica mais alto, 3.5 linhas acima do personagem)
    y_nome = personagem.rect.y - (altura_fonte * 3.5)
    texto_nome = fonte_status.render(personagem.nome, True, (255, 255, 255))
    tela.blit(texto_nome, (personagem.rect.x, y_nome))

    # Configurações das barras
    largura_barra = 60
    altura_barra = 12
    
    # Vida (HP) (Fica 2 linhas acima do personagem)
    cor_hp = (0, 255, 0) if personagem.hp_pct > 0.3 else (255, 0, 0)
    y_hp_barra = personagem.rect.y - (altura_fonte * 2)
    y_hp_texto = y_hp_barra - (altura_fonte // 4) # Ajuste fino para alinhar texto e barra
    
    pygame.draw.rect(tela, (255, 0, 0), (personagem.rect.x, y_hp_barra, largura_barra, altura_barra)) # Fundo
    pygame.draw.rect(tela, cor_hp, (personagem.rect.x, y_hp_barra, largura_barra * personagem.hp_pct, altura_barra)) # Vida atual

    texto_hp = fonte_status.render(f"HP: {personagem.hp}/{personagem.HP_MAX}", True, (255, 255, 255))
    tela.blit(texto_hp, (personagem.rect.x + largura_barra + 10, y_hp_texto))
    
    # Pontos Mágicos (MP) (Fica 1 linha acima do personagem)
    y_mp_barra = personagem.rect.y - altura_fonte
    y_mp_texto = y_mp_barra - (altura_fonte // 4)
    
    pygame.draw.rect(tela, (50, 50, 50), (personagem.rect.x, y_mp_barra, largura_barra, altura_barra)) # Fundo
    pygame.draw.rect(tela, (0, 150, 255), (personagem.rect.x, y_mp_barra, largura_barra * personagem.mp_pct, altura_barra)) # MP atual
    
    texto_mp = fonte_status.render(f"MP: {personagem.mp}", True, (255, 255, 255))
    tela.blit(texto_mp, (personagem.rect.x + largura_barra + 10, y_mp_texto))

    # Textos de Status (Ficam abaixo do personagem)
    texto_status = fonte_status.render(personagem.status_str(), True, (255, 255, 0))
    tela.blit(texto_status, (personagem.rect.x, personagem.rect.bottom + 5))

   
