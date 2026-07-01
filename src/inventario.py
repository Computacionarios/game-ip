
import pygame

#Cores utilizadas ao longo do código
cores = {
    "preto":(0, 0, 0),
    "cinza": (100, 100, 100),
    "cinza_claro": (150, 150, 150),
    "cinza_escuro": (50, 50, 50),
    "branco": (255, 255, 255),
    "amarelo": (255, 255, 0)}

class Inventario:

    def __init__(self):

        self.tamanho_slot = 64   #Tamanho do slot de cada item
        self.espacamento_itens = 5   #Espaçamento entre os slots de itens
        self.linhas = 3   #Números de linhas no inventário
        self.colunas = 3   #Números de colunas no inventário
        self.espaco_player = 150   #Altura onde exibirá o player

        self.aberto = False    #Controle de abertura e fechamento do inventário
        self.menu_aberto = False  #Controle de abertura e fechamento do menu de opções
        self.item_selecionado = None
        self.linha_selecionada = 0
        self.coluna_selecionada = 0
        self.opcao_menu_atual = 0

        self.menu_opcoes = ["Consumir", "Deletar"]    #Menu de opções

        #Superficie do inventário
        inventario_largura = (self.tamanho_slot + self.espacamento_itens) * self.colunas + self.espacamento_itens
        inventario_altura  = (self.tamanho_slot + self.espacamento_itens) * self.linhas + self.espacamento_itens + self.espaco_player
        self.superficie = pygame.Surface((inventario_largura, inventario_altura))    #Define largura e altura da superficie do inventário

        self.inventario_retangular = self.superficie.get_rect(center = (1280 // 2, 720 // 2))    #Inventário definido como um retângulo no centro da tela (pode variar)

        self.sprites_cartas = {}
        self.sprite_player = None

        self.font = pygame.font.Font(None, 18)

        self.itens = []   #Os dicionários com os dados do item

        #dados que vão ser fornecidos pelo game principal
    def definir_sprites_cartas(self, sprites):
        self.sprites_cartas = sprites

    def definir_sprite_player(self, sprite):
        self.sprite_player = sprite
#-------------------------------------------------------

    #Desenha o inventário
    def desenhar_inventario(self, tela):

        if not self.aberto:     #Se o inventário não estiver aberto não executa nada
            return
    
        self.superficie.fill(cores["cinza_escuro"])     #Cor de fundo do inventário
        
        #Desenha o slot do player
        self.desenhar_player()

        #Desenhar os slots
        self.desenhar_slot_inventario()

        #Desenhar itens
        self.desenhar_itens_slot()

        tela.blit(self.superficie, self.inventario_retangular.topleft)    #Exibindo o inventário na tela

        if self.menu_aberto:
            self.desenhar_menu_opcoes(tela)

    #Desenha cada região do item
    def desenhar_slot_inventario(self):

        for linha in range(self.linhas):   #Percorrendo linhas
            for coluna in range(self.colunas):   #Percorrendo colunas
                slot_x = coluna * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens
                slot_y = linha * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens + self.espaco_player
                pygame.draw.rect(self.superficie, cores["cinza"], (slot_x, slot_y, self.tamanho_slot, self.tamanho_slot)) 

                if (linha == self.linha_selecionada and coluna == self.coluna_selecionada):
                    pygame.draw.rect(self.superficie, cores["amarelo"], (slot_x, slot_y, self.tamanho_slot, self.tamanho_slot), 2)

    #Percorre todos os itens do inventário
    def desenhar_itens_slot(self):

        for indice, item in enumerate(self.itens):
            linha = indice // self.colunas
            coluna = indice % self.colunas

            slot_x = coluna * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens
            slot_y = linha * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens + self.espaco_player
            
            sprite = self.sprites_cartas.get(item["sprite"])

            if sprite:
                self.superficie.blit(sprite, (slot_x + 2, slot_y + 2))

            #Desenhar quantidade de itens no slot
            quantidade_texto = self.font.render(str(item["quantidade"]), True, cores["branco"])
            self.superficie.blit(quantidade_texto, (slot_x, slot_y))

    
    def desenhar_menu_opcoes(self, tela):   
        #Desenha o menu de opções do item no inventário 

        menu_opcoes = self.menu_opcoes

        menu_largura = 120
        menu_altura = 25
        menu_x, menu_y = self.menu_posicao

        #Criar um fundo para o menu
        menu_retangular = pygame.Rect(menu_x, menu_y, menu_largura, menu_altura * (len(menu_opcoes)) + self.espacamento_itens * 1.5)
        pygame.draw.rect(tela, cores["preto"], menu_retangular)
        pygame.draw.rect(tela, cores["branco"], menu_retangular, 2)

        for i, opcoes in enumerate(menu_opcoes):
            opcoes_rect = pygame.Rect(menu_x + self.espacamento_itens, menu_y + self.espacamento_itens + i * menu_altura, menu_largura - (self.espacamento_itens * 2), menu_altura - self.espacamento_itens / 2)    #O sitens do menu são variaveis, essa função aceita a troca sem interferir
            pygame.draw.rect(tela, cores["cinza_claro"], opcoes_rect)

            if i == self.opcao_menu_atual:
                pygame.draw.rect(tela, cores["amarelo"], opcoes_rect, 3)

            texto_supercie = self.font.render(opcoes, True, cores["preto"])

            tela.blit(texto_supercie, (menu_x + self.espacamento_itens * 2, menu_y + (menu_altura / 2) + (i * menu_altura)))


    def desenhar_player(self):
        #Desenha a área destinada oa player
        self.player_largura = ((self.tamanho_slot + self.espacamento_itens) * self.colunas - self.espacamento_itens)
        self.player_altura = self.espaco_player - self.espacamento_itens

        #Desenha slot do player
        pygame.draw.rect(self.superficie, cores["cinza"], (self.espacamento_itens, self.espacamento_itens, self.player_largura, self.player_altura))

        if self.sprite_player:
            
            sprite = self.sprite_player

            sprite_x = self.espacamento_itens + (self.player_largura - sprite.get_width()) // 2
            sprite_y = self.espacamento_itens + (self.player_altura - sprite.get_height()) // 2


            self.superficie.blit(sprite, (sprite_x, sprite_y))


    def menu_acoes(self):
        #Executa uma ação selecionado no menu
        opcao = self.menu_opcoes[self.opcao_menu_atual]

        #Envia qual item foi consumido, para executar a ação no jogo
        if opcao == "Consumir":
            return {"acao": "Consumir", "item": self.consumir_item()}

        if opcao == "Deletar":
            self.remove_itens(self.item_selecionado["id"])
            self.item_selecionado = None
            self.menu_aberto = False

            return {"acao": "Deletar"}

    #Função consumir que informa qual item foi consumido, para tomada de decisão do código principal
    def consumir_item(self):
        
        item = self.item_selecionado.copy()

        self.remove_itens(self.item_selecionado["id"])
        self.item_selecionado = None
        self.menu_aberto = False

        return item

    #Cria menu de opções 
    def cria_menu(self, item):
        #Cria as opções do menu de acordo com o tipo da carta
        
        return ["Consumir", "Deletar"]

    #Controle de abertura e fechamento do inventário
    def abre_fecha_inventario(self):
        self.aberto = not self.aberto

    #Adiciona itens encontrados
    def adicionar_itens(self, id, sprite, nome, quantidade = 1):
        #id: identificador da imagem
        #nome: nome da carta
        #quantidade: quantidade de itens a adicionar

        for item in self.itens:
            if item["id"] == id:
                item["quantidade"] += quantidade
                return
            
        self.itens.append ({
            "id": id,
            "sprite": sprite,
            "nome": nome,
            "quantidade": quantidade
        })

    #Remove itens 
    def remove_itens(self, id, quantidade = 1):
        #id: identificador da imagem
        #nome: nome da carta
        #tipo: tipo da carta
        #quantidade: quantidade de itens a adicionar

        for item in self.itens:
            if item["id"] == id:
                item["quantidade"] -= quantidade
                if item["quantidade"] <= 0:
                    self.itens.remove(item)
                return

    #Verifica tecla que o usuário escolheu para selicionar a ação
    def captura_evento(self, evento):

        if not self.aberto:
            return
        
        if evento.type == pygame.KEYDOWN:

             #Menu aberto
            if self.menu_aberto:
            
                #Seta para cima no menu
                if evento.key == pygame.K_UP:
                    self.opcao_menu_atual = max(0, self.opcao_menu_atual - 1)

                #Seta para baixo no menu
                elif evento.key == pygame.K_DOWN:
                    self.opcao_menu_atual = min(len(self.menu_opcoes) - 1, self.opcao_menu_atual + 1)

                #Se clicar em enter no menu, acontece algo com o player
                elif evento.key == pygame.K_RETURN:

                    return self.menu_acoes()
                   
                #Tecla esc para fechar o menu de opções
                elif evento.key == pygame.K_ESCAPE:
                    self.menu_aberto = False

            else:
                #Seta para esquerda 
                if evento.key == pygame.K_LEFT: 
                    self.coluna_selecionada = max(0, self.coluna_selecionada - 1)

                #Seta para direita
                elif evento.key == pygame.K_RIGHT:
                    self.coluna_selecionada = min(self.colunas -1, self.coluna_selecionada + 1)

                #Seta para cima
                elif evento.key == pygame.K_UP: 
                    self.linha_selecionada = max(0, self.linha_selecionada - 1)

                #Seta para baixo
                elif evento.key == pygame.K_DOWN:
                    self.linha_selecionada = min(self.linhas - 1, self.linha_selecionada + 1)

                #Se clicar enter seleciona a carta e exibi menu de opções
                elif evento.key == pygame.K_RETURN:
                    indice = (self.linha_selecionada * self.colunas + self.coluna_selecionada)

                    if indice < len(self.itens):
            
                        slot_x = self.coluna_selecionada * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens
                        slot_y = self.linha_selecionada * (self.tamanho_slot + self.espacamento_itens) + self.espacamento_itens + self.espaco_player

                        self.menu_posicao = (self.inventario_retangular.left + slot_x + self.tamanho_slot + 10, self.inventario_retangular.top + slot_y)

                        self.item_selecionado = self.itens[indice]
                        self.menu_opcoes = self.cria_menu(self.item_selecionado)
                        self.menu_aberto = True
                        self.opcao_menu_atual = 0



