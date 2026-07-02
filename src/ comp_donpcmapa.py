# arquivo que a partir da colisão inicia o combate o retorna para a tela de exploração

import pygame
import sys
from batalha import Batalha, renderizar_batalha 

class  comp_donpcmapa:
    def __init__(self, tela, velocidade, percurso, npc_larg_hitbox, npc_alt_hitbox):  

        #Tela em que o rect será gerado
        self.tela = tela

        ##Atributos do NPC
        self.velocidade = velocidade
        self.percurso = percurso
        self.npc_larg_hitbox = npc_larg_hitbox
        self.npc_alt_hitbox = npc_alt_hitbox
        
        #Sentido de movimentação padrão ( quando chegar ao final, a ordem será trocada)
        self.sentido_domovimento = 'D'  

        #Index da ponto no mapa
        self.index_doponto = 0

        #Criação da hitbox
        self.NPChitbox = pygame.Rect(self.percurso[self.index_doponto][0], self.percurso[self.index_doponto][1], self.npc_larg_hitbox, self.npc_alt_hitbox)

    #Função que atualiza a posição do npc no mapa
    def atualizar(self, player):
        
        pygame.draw.rect(self.tela, (255,0,0), self.NPChitbox)
        
        if self.NPChitbox.colliderect(player):
           return True # Avisa ao loop principal que a batalha deve começar
            

        else:
            
            #Se o NPC chegar em algum ponto, então ele se locomoverá para outro a partir de agora.
            if self.NPChitbox.x == self.percurso[self.index_doponto][0] and self.NPChitbox.y == self.percurso[self.index_doponto][1]:
                
                if self.index_doponto == len(self.percurso)  - 1:
                    self.sentido_domovimento = 'E'

                if self.sentido_domovimento == 'D':  
                        self.index_doponto += 1

                elif self.sentido_domovimento == 'E':
                    if self.index_doponto != 0:
                        self.index_doponto -= 1
                    else:
                        self.sentido_domovimento = 'D'
            else:

                #Movimentação em no eixo x
                if self.NPChitbox.x > self.percurso[self.index_doponto][0]:
                    self.NPChitbox.x -= self.velocidade
                elif self.NPChitbox.x < self.percurso[self.index_doponto][0]:
                    self.NPChitbox.x += self.velocidade    
                                
                #Movimentação em no eixo y
                elif self.NPChitbox.y > self.percurso[self.index_doponto][1]:
                    self.NPChitbox.y -= self.velocidade
                elif self.NPChitbox.y < self.percurso[self.index_doponto][1]:
                    self.NPChitbox.y += self.velocidade

            return False # Batalha não iniciada
        
#  NOVO LOOP PRINCIPAL DO JOGO
def iniciar_jogo():
    pygame.init()
    
    LARGURA_INICIAL, ALTURA_INICIAL = 1920, 1080
    tela = pygame.display.set_mode((LARGURA_INICIAL, ALTURA_INICIAL), pygame.RESIZABLE)
    pygame.display.set_caption("Exploração e Batalha Elemental")
    
    relogio = pygame.time.Clock()
    FPS = 60 
    
    try:
        fonte_log = pygame.font.SysFont("segoeuiemoji", 28) 
        fonte_carta_desc = pygame.font.SysFont("arial", 16)
    except:
        fonte_log = pygame.font.Font(None, 32)
        fonte_carta_desc = pygame.font.Font(None, 20)
        
    # Variáveis de Exploração (Mapa)
    jogador_mapa = pygame.Rect(400, 300, 50, 80) # Hitbox do jogador no mapa
    vel_jogador = 7
    
    percurso_npc = [(100, 100), (800, 100), (800, 500), (100, 500)]
    npc = comp_donpcmapa(tela, 5, percurso_npc, 50, 80)
    npc_ativo = True # Controla se o NPC ainda existe no mapa
    
    # Gerenciador de Estados
    estado_jogo = "EXPLORACAO" # Começa no mapa
    instancia_batalha = None

    #  variaveis para o controle do fade
    em_transicao = False
    alpha_fade = 0
    fade_speed = 10 # Controla o quão rápido a tela escurece/clareia
    estado_destino = None

    rodando = True
    while rodando:
        LARGURA, ALTURA = tela.get_size()
        
        # Cores dinâmicas de fundo dependendo do estado
        COR_FUNDO = (30, 30, 40) if estado_jogo == "BATALHA" else (50, 150, 70)
        tela.fill(COR_FUNDO)
        
        # PROCESSAMENTO DE EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.VIDEORESIZE:
                tela = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
                
            # Inputs específicos de Batalha (Bloqueados durante o fade)
            if estado_jogo == "BATALHA" and not em_transicao:
                if evento.type == pygame.KEYDOWN:
                    if instancia_batalha.aguardando_input:
                        if (evento.key == pygame.K_LEFT) or (evento.key == pygame.K_a):
                            instancia_batalha.input("esquerda")
                        elif (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_d):
                            instancia_batalha.input("direita")
                        elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                            instancia_batalha.input("usar")
                    elif instancia_batalha.encerrada:
                        # Se a batalha acabou, pressionar ESC ou ENTER inicia o Fade para voltar
                        if evento.key in (pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_SPACE):
                            em_transicao = True
                            estado_destino = "EXPLORACAO"

        # LÓGICA E RENDERIZAÇÃO POR ESTADO
        if estado_jogo == "EXPLORACAO":
            
            # Movimentação do jogador (Bloqueada durante o fade)
            if not em_transicao:
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: jogador_mapa.x -= vel_jogador
                if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: jogador_mapa.x += vel_jogador
                if teclas[pygame.K_UP] or teclas[pygame.K_w]: jogador_mapa.y -= vel_jogador
                if teclas[pygame.K_DOWN] or teclas[pygame.K_s]: jogador_mapa.y += vel_jogador

            # Desenha o Jogador na cor Azul
            pygame.draw.rect(tela, (0, 128, 255), jogador_mapa)

            # Atualiza o NPC e checa colisão
            if npc_ativo:
                iniciou_batalha = npc.atualizar(jogador_mapa)
                # Só inicia a transição se já não estiver em uma
                if iniciou_batalha and not em_transicao:
                    em_transicao = True
                    estado_destino = "BATALHA"

        elif estado_jogo == "BATALHA":
            # Roda a lógica e a renderização da batalha
            instancia_batalha.tick()
            renderizar_batalha(tela, instancia_batalha, LARGURA, ALTURA, fonte_log, fonte_carta_desc)

        # --- fade renderizada por cima do jogo ---
        if em_transicao:
            # Cria a superfície do fade no tamanho atual da tela (útil se foi redimensionada)
            superficie_fade = pygame.Surface((LARGURA, ALTURA))
            superficie_fade.fill((0, 0, 0)) # Cor do Fade (Preto)

            if estado_jogo != estado_destino:
                # TELA ESCURECENDO (Fade OUT)
                alpha_fade += fade_speed
                if alpha_fade >= 255:
                    alpha_fade = 255
                    estado_jogo = estado_destino # Efetua a troca de estado oculta no escuro
                    
                    # Inicializações dependentes do estado
                    if estado_jogo == "BATALHA":
                        instancia_batalha = Batalha("Herói")
                    elif estado_jogo == "EXPLORACAO":
                        npc_ativo = False # Remove o NPC derrotado do mapa
            else:
                # TELA CLAREANDO (Fade IN)
                alpha_fade -= fade_speed
                if alpha_fade <= 0:
                    alpha_fade = 0
                    em_transicao = False # Encerra o fade e devolve o controle ao jogador

            superficie_fade.set_alpha(alpha_fade)
            tela.blit(superficie_fade, (0, 0))


        # ATUALIZAÇÃO DA TELA
        pygame.display.flip()
        relogio.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_jogo()
        

        


