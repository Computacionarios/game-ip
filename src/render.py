# arquivo render.py criado para separar a renderização de imagens - teste

import pygame
import sys
from batalha import Batalha, renderizar_batalha

# CÓDIGO DE INTEGRAÇÃO COM O PYGAME FOI MOVIDO PARA CÁ
def iniciar_jogo():
    pygame.init()
    
    # Configurações de Tela adaptáveis
    # Iniciando com uma resolução razoável (1920x1080) mas com suporte a redimensionamento
    LARGURA_INICIAL, ALTURA_INICIAL = 1920, 1080
    tela = pygame.display.set_mode((LARGURA_INICIAL, ALTURA_INICIAL), pygame.RESIZABLE)
    pygame.display.set_caption("Batalha de Cartas Elementais")
    
    # Controle de FPS (Frames Por Segundo)
    relogio = pygame.time.Clock()
    FPS = 60 
    
    # Fontes e Cores
    try:
        fonte_log = pygame.font.SysFont("segoeuiemoji", 28) 
        fonte_carta_desc = pygame.font.SysFont("arial", 16)
    except:
        fonte_log = pygame.font.Font(None, 32)
        fonte_carta_desc = pygame.font.Font(None, 20)
        
    COR_FUNDO = (30, 30, 40)
    
    # Instancia a Batalha
    batalha = Batalha("Herói")

    rodando = True
    while rodando:
        # Pega as dimensões de forma responsiva a cada frame
        LARGURA, ALTURA = tela.get_size()
        
        # PROCESSAMENTO DE EVENTOS (Inputs)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            # Atualização no modo de janela se for redimensionada
            if evento.type == pygame.VIDEORESIZE:
                tela = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
            if evento.type == pygame.KEYDOWN:
                if batalha.aguardando_input:
                    if (evento.key == pygame.K_LEFT) or (evento.key == pygame.K_a):
                        batalha.input("esquerda")
                    elif (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_d):
                        batalha.input("direita")
                    elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                        batalha.input("usar")
                elif batalha.encerrada:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
        # ATUALIZAÇÃO DA LÓGICA (Tick)
        batalha.tick()
        # 3. RENDERIZAÇÃO
        tela.fill(COR_FUNDO)
        # Chama a função de renderização passando as dimensões atuais
        renderizar_batalha(tela, batalha, LARGURA, ALTURA, fonte_log, fonte_carta_desc)
        # Atualiza a janela
        pygame.display.flip()
        relogio.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_jogo()
