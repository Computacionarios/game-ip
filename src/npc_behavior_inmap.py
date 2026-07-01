import pygame

class npc_behavior_inmap:
    def __init__(self, screen, speed, percurso, npc_larg_hitbox, npc_alt_hitbox):  

        #Tela em que o rect será gerado
        self.screen = screen

        ##Atributos do NPC
        self.speed = speed
        self.percurso = percurso
        self.npc_larg_hitbox = npc_larg_hitbox
        self.npc_alt_hitbox = npc_alt_hitbox
        
        #Sentido de movimentação padrão ( quando chegar ao final, a ordem será trocada)
        self.sentido_domovimento = '->'  

        #Index da ponto no mapa
        self.index_doponto = 0

        #Criação da hitbox
        self.npcRect = pygame.Rect(self.percurso[self.index_doponto][0], self.percurso[self.index_doponto][1], self.npc_larg_hitbox, self.npc_alt_hitbox)

    #Função que atualiza a posição do npc no mapa
    def atualizar(self, player):
        
        pygame.draw.rect(self.screen, (255,0,0), self.npcRect)
        
        if self.npcRect.colliderect(player):

            print("Batalha iniciada!")

        else:
            
            #Se o NPC chegar em algum ponto, então ele se locomoverá para outro a partir de agora.
            if self.npcRect.x == self.percurso[self.index_doponto][0] and self.npcRect.y == self.percurso[self.index_doponto][1]:
                
                if self.index_doponto == len(self.percurso)  - 1:
                    self.sentido_domovimento = '<-'

                if self.sentido_domovimento == '->':  
                        self.index_doponto += 1

                elif self.sentido_domovimento == '<-':
                    if self.index_doponto != 0:
                        self.index_doponto -= 1
                    else:
                        self.sentido_domovimento = '->'
            else:
                #Movimentação em x
                if self.npcRect.x > self.percurso[self.index_doponto][0]:
                    self.npcRect.x -= self.speed
                elif self.npcRect.x < self.percurso[self.index_doponto][0]:
                    self.npcRect.x += self.speed                
                #Movimentação em y
                elif self.npcRect.y > self.percurso[self.index_doponto][1]:
                    self.npcRect.y -= self.speed
                elif self.npcRect.y < self.percurso[self.index_doponto][1]:
                    self.npcRect.y += self.speed

            print(self.npcRect.x, self.npcRect.y)
            print((self.index_doponto))
        

        


