import pygame

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

            print("Batalha iniciada!")

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

            print(self.NPChitbox.x, self.NPChitbox.y)
            print((self.index_doponto))
        

        


