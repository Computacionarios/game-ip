# arquivo cartas modificado para pygame - teste

import pygame
# from efeitos import Queimadura # sem uso no momento falta criar o arquivo de efeitos


class Carta(pygame.sprite.Sprite): # classe base de carta
    def __init__(self, nome, tipo, descricao, x=0, y=0):
        super().__init__()
        self.nome = nome
        self.tipo = tipo          
        self.descricao = descricao

        # --- Atributos Visuais do Pygame ---
        self.image = pygame.Surface((150, 220)) # Tamanho padrão da carta (largura, altura)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) # Posição X e Y da carta na tela

        # Define cores de fundo automáticas baseadas no tipo da carta
        if self.tipo == "ataque":
            self.image.fill((180, 50, 50))    # Vermelho
        elif self.tipo == "defesa":
            self.image.fill((50, 50, 180))    # Azul
        elif self.tipo == "cura":
            self.image.fill((50, 150, 50))    # Verde
        else:
            self.image.fill((120, 50, 150))   # Roxo para Especial

    def usar(self, usuario, alvo, estado):
        """Retorna (mensagem: str, sucesso: bool)"""
        raise NotImplementedError

    def desenhar(self, tela, fonte_nome, fonte_desc):
        """Método para desenhar a carta e seus textos na tela do Pygame"""
        # Desenha o corpo (retângulo) da carta
        tela.blit(self.image, self.rect)
        
        # Desenha o nome da carta
        texto_nome = fonte_nome.render(self.nome, True, (255, 255, 255))
        tela.blit(texto_nome, (self.rect.x + 10, self.rect.y + 10))
        
        # Desenha a descrição (completando o visual)
        texto_desc = fonte_desc.render(self.descricao, True, (240, 240, 240))
        tela.blit(texto_desc, (self.rect.x + 10, self.rect.y + 180))


class ChamaInfernal(Carta):
    def __init__(self, x=0, y=0):
        super().__init__("Chama Infernal", "ataque",
                         "15 dano + queimadura (3t·4/t) | conta fogo", x, y)

    def usar(self, usuario, alvo, estado):
        dano = max(0, 15 - alvo.defesa_atual)
        alvo.receber_dano(dano)
        alvo.defesa_atual = 0
        usuario.usos_fogo += 1

        msg = f"{usuario.nome} usou Chama Infernal! (-{dano} HP)"
        #if not any(isinstance(e, Queimadura) for e in alvo.efeitos):
        #    alvo.efeitos.append(Queimadura())
        #    msg += " + queimadura!"
        return msg, True


class TempestadeRelampago(Carta):
    def __init__(self, x=0, y=0):
        super().__init__("Tempestade Relâmpago", "ataque",
                         "35 dano | req 2x Chama | Speed +10 / inimigo -10", x, y)

    def usar(self, usuario, alvo, estado):
        if usuario.usos_fogo < 2:
            return "Requer 2 usos de Chama Infernal!", False
        dano = max(0, 35 - alvo.defesa_atual)
        alvo.receber_dano(dano)
        alvo.defesa_atual = 0
        usuario.speed = min(100, usuario.speed + 10)
        alvo.speed    = max(0,   alvo.speed   - 10)
        return f"{usuario.nome} usou Tempestade Relâmpago! (-{dano} HP) Speed ±10", True


class ColapsoTitanico(Carta):
    def __init__(self, x=0, y=0):
        super().__init__("Colapso Titânico", "ataque",
                         "70 dano | req 5x Chama | uso único", x, y)
        self.usado = False

    def usar(self, usuario, alvo, estado):
        if usuario.usos_fogo < 5:
            return "Requer 5 usos de Chama Infernal!", False
        if self.usado:
            return "Colapso Titânico já foi usado!", False
        dano = max(0, 70 - alvo.defesa_atual)
        alvo.receber_dano(dano)
        alvo.defesa_atual = 0
        self.usado = True
        return f"{usuario.nome} usou Colapso Titânico! (-{dano} HP) DEVASTADOR!", True


#DEFESA
class Escudo(Carta): # defesa de maior eficácia porém concentrada em uma área menor
    def __init__(self, x=0, y=0):
        super().__init__("Escudo", "defesa", "+50 defesa neste turno", x, y)

    def usar(self, usuario, alvo, estado): 
        usuario.defesa_atual = 50
        return f"{usuario.nome} ativou Escudo! (+50 def)", True


class Barreira(Carta):  # defesa de eficácia mediana e de área de proteção intermediaria 
    def __init__(self, x=0, y=0):
        super().__init__("Barreira", "defesa", "+25 defesa neste turno", x, y)

    def usar(self, usuario, alvo, estado):
        usuario.defesa_atual = 25
        return f"{usuario.nome} ativou Barreira! (+25 def)", True


class DomoProtetor(Carta): # defesa de menor eficácia mas é a mais abrangente em questão de área coberta
    def __init__(self, x=0, y=0):
        super().__init__("Domo Protetor", "defesa", "+ 15 def", x, y)

    def usar(self, usuario, alvo, estado):
        usuario.defesa_atual = 15
        return f"{usuario.nome} ativou Domo Protetor! (+ 15 def)", True


#CURA
class CuraPequena(Carta): 
    def __init__(self, x=0, y=0):
        super().__init__("Cura Pequena", "cura", "Recupera 20 HP", x, y)

    def usar(self, usuario, alvo, estado):
        ganho = usuario.curar(20)
        return f"{usuario.nome} usou Cura Pequena! (+{ganho} HP)", True


class CuraGrande(Carta):
    def __init__(self, x=0, y=0):
        super().__init__("Cura Grande", "cura", "Recupera 35 HP", x, y)

    def usar(self, usuario, alvo, estado):
        ganho = usuario.curar(35)
        return f"{usuario.nome} usou Cura Grande! (+{ganho} HP)", True


# ESPECIAL
class Fuga(Carta):
    def __init__(self, x=0, y=0):
        super().__init__("Fuga", "especial", "Sai imediatamente da batalha", x, y)

    def usar(self, usuario, alvo, estado):
        estado["fugiu"] = True
        return f"{usuario.nome} fugiu da batalha!", True


#DECK PADRÃO
def criar_deck():
    return [
        ChamaInfernal(),
        TempestadeRelampago(),
        ColapsoTitanico(),
        Escudo(),
        Barreira(),
        DomoProtetor(),
        CuraPequena(),
        CuraGrande(),
        Fuga(),
    ]

