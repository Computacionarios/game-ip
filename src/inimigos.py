# arquivo dos inimigos alterados para o uso da biblioteca pygame - teste

import random
from .jogador import Personagem

class CPU(Personagem): 
    def __init__(self, tipo_inimigo, elemento_inimigo, vida_inimigo, nome, x=0, y=0): 

        self.HP_MAX = vida_inimigo
        super().__init__(nome, x, y)         
        self.escolha_acao = None
        self.escolha_forma = None
        self.escolha_elemento = None

        #Pode ser, somente, do tipo comum ou boss
        self.tipo_inimigo = tipo_inimigo

        #Pode ser, somente, do elemento raio ou metal ou borracha
        self.elemento_inimigo = elemento_inimigo
        
        self.image.fill((220, 50, 50)) 

    def escolher_combo(self):
        # A IA escolhe seu combo levando em conta seus Pontos Mágicos (MP)
        # Ação: Cura crítica - o inimigo tenta se curar se estiver com pouca vida
        # Mesmo com o menu do jogador usando a aba Utilitários, 
        # internamente e para a IA essa ação se resolve chamando "cura"
        if self.tipo_inimigo == "comum":

            if self.hp_pct < 0.30:
                self.escolha_acao = "cura"
            elif random.random() < 0.22:
                self.escolha_acao = "defesa"
            else:
                self.escolha_acao = "ataque"

            # 2. Forma (Gerenciamento de MP)
            opcoes_forma = []
            if self.mp >= 6: opcoes_forma.append("triangulo")
            if self.mp >= 4: opcoes_forma.append("quadrado")
            if self.mp >= 2: opcoes_forma.append("circulo")
            
            if not opcoes_forma:
                self.escolha_forma = "circulo" 
            else:
                self.escolha_forma = random.choice(opcoes_forma)
        else:

            if self.hp_pct < 0.50:
                self.escolha_acao = "cura"
            elif random.random() < 0.10:
                self.escolha_acao = "defesa"
            else:
                self.escolha_acao = "ataque"

            # 2. Forma (Gerenciamento de MP)
            opcoes_forma = []
            if self.mp >= 6: opcoes_forma.append("triangulo")
            if self.mp >= 4: opcoes_forma.append("quadrado")
            if self.mp >= 2: opcoes_forma.append("circulo")
            
            if not opcoes_forma:
                self.escolha_forma = "circulo" 
            else:
                self.escolha_forma = random.choice(opcoes_forma)

        # 3. Elemento
        elementos = ["raio", "metal", "borracha"]
        
        a = 0
        b = 0
        c = 0

        if self.elemento_inimigo == elementos[0]:
            a = 100
        elif self.elemento_inimigo == elementos[1]:
            b = 100
        elif self.elemento_inimigo == elementos[2]:
            c = 100

        if self.escolha_acao == "ataque":
            self.escolha_elemento = random.choices(elementos, weights=[a, b, c])[0]
        elif self.escolha_acao == "defesa":
            self.escolha_elemento = random.choices(elementos, weights=[a, b, c])[0]
        else:
            self.escolha_elemento = random.choices(elementos, weights=[a, b, c])[0]
