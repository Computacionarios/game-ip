import pygame

###COLETAVEL###

def coletavel_cura():
    return [
        pygame.image.load("assets/images/Coletavel/Forma/one.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Forma/two.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Forma/three.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Forma/four.png").convert_alpha()
        ]

def coletavel_imunidade():
    return [
        pygame.image.load("assets/images/Coletavel/Elemental/one.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Elemental/two.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Elemental/three.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Elemental/four.png").convert_alpha()
    ]

def coletavel_mana():
    return [
        pygame.image.load("assets/images/Coletavel/Utilitario/one.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Utilitario/two.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Utilitario/three.png").convert_alpha(),
        pygame.image.load("assets/images/Coletavel/Utilitario/four.png").convert_alpha()
    ]

###PLAYER###

def movimento_player():
    run_costas = [
        pygame.image.load("assets/images/Player/corrida_atras(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_atras(3).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_atras(1).png").convert_alpha(),
    ]

    run_direita = [
        pygame.image.load("assets/images/Player/corrida_direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_direita(3).png").convert_alpha(),
    ]

    run_esquerda = [
        pygame.image.load("assets/images/Player/corrida_esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_esquerda(3).png").convert_alpha(),
    ]

    run_frente = [
        pygame.image.load("assets/images/Player/corrida_frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/corrida_frente(3).png").convert_alpha(),
    ]

    parado = [
        pygame.image.load("assets/images/Player/parado_frente.png").convert_alpha(),
        pygame.image.load("assets/images/Player/parado_esquerda.png").convert_alpha(),
        pygame.image.load("assets/images/Player/parado_direita.png").convert_alpha(),
        pygame.image.load("assets/images/Player/parado_costas.png").convert_alpha()
    ]

    return run_costas, run_frente, run_esquerda, run_direita, parado

def ataque_player():
    frente = [
        pygame.image.load("assets/images/Player/Ataque/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(6).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/frente(7).png").convert_alpha()
    ]

    costas = [
        pygame.image.load("assets/images/Player/Ataque/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(6).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/costas(7).png").convert_alpha()
    ]

    esquerda = [
        pygame.image.load("assets/images/Player/Ataque/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(6).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/esquerda(7).png").convert_alpha()
    ]

    direita = [
        pygame.image.load("assets/images/Player/Ataque/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(6).png").convert_alpha(),
        pygame.image.load("assets/images/Player/Ataque/direita(7).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

###INIMIGOS###

##BOSS##

#ELETRICO#
def ataque_boss_eletrico():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(11).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/frente(12).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(11).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/costas(12).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(11).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/direita(12).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(11).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Ataque/esquerda(12).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def morte_boss_eletrico():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/frente(11).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/costas(11).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/direita(11).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(8).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(9).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(10).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Morte/esquerda(11).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def andar_boss_eletrico():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Andando/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def andar_boss_eletrico():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/frente(3).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/costas(2).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/direita(2).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Eletrico/Parado/esquerda(2).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

#AÇO#
def ataque_boss_aco():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/frente(8).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/costas(8).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/direita(8).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(6).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(7).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Ataque/esquerda(8).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def andar_boss_aco():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Andando/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita


def parado_boss_aco():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/frente(4).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/costas(4).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/direita(4).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Parado/esquerda(4).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def morte_boss_aco():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Aco/Morte/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

#BORRACHA#
def ataque_boss_borracha():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Ataque/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def morte_boss_borracha():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Morte/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def parado_boss_borracha():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/frente(2).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/costas(2).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/direita(2).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Parado/esquerda(2).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

def andar_boss_borracha():
    frente= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/frente(6).png").convert_alpha()
    ]
    costas = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/costas(6).png").convert_alpha()
    ]
    direita = [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/direita(6).png").convert_alpha()
    ]
    esquerda= [
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(1).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(2).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(3).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(4).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(5).png").convert_alpha(),
        pygame.image.load("assets/images/Inimigos/Boss/Borracha/Andando/esquerda(6).png").convert_alpha()
    ]
    return frente, costas, esquerda, direita

##SLIME##

#ELETRICO#
def andar_slime_borracha():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Andando/frente({i+1}).png").convert_alpha() for i in range(8)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Andando/costas({i+1}).png").convert_alpha() for i in range(8)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Andando/direita({i+1}).png").convert_alpha() for i in range(8)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Andando/esquerda({i+1}).png").convert_alpha() for i in range(8)]

    return frente, costas, esquerda, direita

def morte_slime_borracha():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Morte/frente({i+1}).png").convert_alpha() for i in range(10)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Morte/direita({i+1}).png").convert_alpha() for i in range(10)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Morte/esquerda({i+1}).png").convert_alpha() for i in range(10)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Morte/costas({i+1}).png").convert_alpha() for i in range(10)]

    return frente, costas, esquerda, direita

def parado_slime_borracha():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Parado/frente({i+1}).png").convert_alpha() for i in range(6)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Parado/direita({i+1}).png").convert_alpha() for i in range(6)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Parado/esquerda({i+1}).png").convert_alpha() for i in range(6)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Parado/costas({i+1}).png").convert_alpha() for i in range(6)]

    return frente, costas, esquerda, direita

def atacando_slime_borracha():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Atacando/frente({i+1}).png").convert_alpha() for i in range(11)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Atacando/direita({i+1}).png").convert_alpha() for i in range(11)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Atacando/esquerda({i+1}).png").convert_alpha() for i in range(11)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Borracha/Atacando/costas({i+1}).png").convert_alpha() for i in range(11)]

    return frente, costas, esquerda, direita

#AÇO#
def andar_slime_aco():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Andando/frente({i+1}).png").convert_alpha() for i in range(8)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Andando/costas({i+1}).png").convert_alpha() for i in range(8)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Andando/direita({i+1}).png").convert_alpha() for i in range(8)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Andando/esquerda({i+1}).png").convert_alpha() for i in range(8)]

    return frente, costas, esquerda, direita

def morte_slime_aco():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Morte/frente({i+1}).png").convert_alpha() for i in range(10)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Morte/direita({i+1}).png").convert_alpha() for i in range(10)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Morte/esquerda({i+1}).png").convert_alpha() for i in range(10)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Morte/costas({i+1}).png").convert_alpha() for i in range(10)]

    return frente, costas, esquerda, direita

def parado_slime_aco():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Parado/frente({i+1}).png").convert_alpha() for i in range(6)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Parado/direita({i+1}).png").convert_alpha() for i in range(6)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Parado/esquerda({i+1}).png").convert_alpha() for i in range(6)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Parado/costas({i+1}).png").convert_alpha() for i in range(6)]

    return frente, costas, esquerda, direita

def atacando_slime_aco():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Atacando/frente({i+1}).png").convert_alpha() for i in range(10)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Atacando/direita({i+1}).png").convert_alpha() for i in range(10)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Atacando/esquerda({i+1}).png").convert_alpha() for i in range(10)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Aco/Atacando/costas({i+1}).png").convert_alpha() for i in range(10)]

    return frente, costas, esquerda, direita

#ELETRICO#
def andar_slime_eletrico():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Andando/frente({i+1}).png").convert_alpha() for i in range(8)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Andando/costas({i+1}).png").convert_alpha() for i in range(8)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Andando/direita({i+1}).png").convert_alpha() for i in range(8)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Andando/esquerda({i+1}).png").convert_alpha() for i in range(8)]

    return frente, costas, esquerda, direita

def morte_slime_eletrico():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Morte/frente({i+1}).png").convert_alpha() for i in range(10)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Morte/direita({i+1}).png").convert_alpha() for i in range(10)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Morte/esquerda({i+1}).png").convert_alpha() for i in range(10)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Morte/costas({i+1}).png").convert_alpha() for i in range(10)]

    return frente, costas, esquerda, direita

def parado_slime_eletrico():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Parado/frente({i+1}).png").convert_alpha() for i in range(6)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Parado/direita({i+1}).png").convert_alpha() for i in range(6)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Parado/esquerda({i+1}).png").convert_alpha() for i in range(6)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Parado/costas({i+1}).png").convert_alpha() for i in range(6)]

    return frente, costas, esquerda, direita

def atacando_slime_eletrico():
    frente = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Atacando/frente({i+1}).png").convert_alpha() for i in range(9)]
    direita = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Atacando/direita({i+1}).png").convert_alpha() for i in range(9)]
    esquerda = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Atacando/esquerda({i+1}).png").convert_alpha() for i in range(9)]
    costas = [pygame.image.load(f"assets/images/Inimigos/Slime/Eletrico/Atacando/costas({i+1}).png").convert_alpha() for i in range(9)]

    return frente, costas, esquerda, direita