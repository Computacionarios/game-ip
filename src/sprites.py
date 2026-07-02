import pygame
from pathlib import Path


def listar(path: str):
  frames = []

  for idx, item in enumerate(Path(path).iterdir()):
    if item.is_file() and item.name[0].isdigit():
      frames.append(pygame.image.load(f"{path}/{idx}.png").convert_alpha())
    return frames


ELETRICO = "Eletrico"
METAL = "Metal"
BORRACHA = "Borracha"

BOSS = "Boss"
SLIME = "Slime"

FRENTE = "Frente"
COSTAS = "Costas"
DIREITA = "Direita"
ESQUERDA = "Esquerda"
PARADO = "Parado"

ATACAR = "Atacar"
DEFENDER = "Defender"
USAR = "Usar"


class Inimigo:
  def __init__(self, raca, tipo):
    self.raca = raca
    self.tipo = tipo

  def parado(self):
    return listar(f"assets/images/Inimigos/{self.raca}/{self.tipo}/Parado")

  def atacando(self):
    return listar(f"assets/images/Inimigos/{self.raca}/{self.tipo}/Ataque")

  def morrendo(self):
    return listar(f"assets/images/Inimigos/{self.raca}/{self.tipo}/Morte")


class Coletavel:
  def util(self):
    return listar("assets/images/Coletavel/Utilitario")

  def elemento(self):
    return listar("assets/images/Coletavel/Elemental")

  def forma(self):
    return listar("assets/images/Coletavel/Forma")


class Player:
  def andando(self, direcao):
    return listar(f"assets/images/Player/Andando/{direcao}")

  def parado(self, direcao):
    return listar(f"assets/images/Player/Parado/{direcao}")

  def atacando(self):
    return listar("assets/images/Player/Atacando")
