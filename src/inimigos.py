# arquivo dos inimigos alterados para o uso da biblioteca pygame - teste
import random
from .jogador import Personagem
from .cartas import (
  ChamaInfernal,
  TempestadeRelampago,
  ColapsoTitanico,
  Escudo,
  Barreira,
  DomoProtetor,
  CuraPequena,
  CuraGrande,
)


class CPU(Personagem):
  def __init__(self, nome="CPU", x=0, y=0):
    super().__init__(nome, x, y)  # Passa os argumentos para a classe mãe (Personagem)
    self.ultima_carta_usada = None

    # --- Adaptação Visual Pygame ---
    # Como o Personagem original é azul,o inimigo será vermelho, para diferenciá-los visualmente na tela de combate
    self.image.fill((220, 50, 50))

  def _idx(self, *tipos):
    for t in tipos:
      for i, c in enumerate(self.deck):
        if isinstance(c, t):
          return i
    return None

  def escolher_carta(self):
    # Cura crítica - o ininmigo tenta se curar se estiver com pouca vida
    if self.hp_pct < 0.30:
      idx = self._idx(CuraGrande, CuraPequena)
      if idx is not None:
        self.idx_carta = idx
        return

    # Colapso Titânico
    if self.usos_fogo >= 5:
      idx = self._idx(ColapsoTitanico)
      if idx is not None:
        colapso = self.deck[idx]
        if not colapso.usado:
          self.idx_carta = idx
          return

    # Tempestade Relâmpago
    if self.usos_fogo >= 2 and random.random() < 0.55:
      idx = self._idx(TempestadeRelampago)
      if idx is not None:
        self.idx_carta = idx
        return

    # Defesa ocasional
    if random.random() < 0.22:
      opcoes = [
        i
        for i, c in enumerate(self.deck)
        if isinstance(c, (Escudo, Barreira, DomoProtetor))
      ]
      if opcoes:
        self.idx_carta = random.choice(opcoes)
        return

    # Padrão: Chama Infernal
    idx = self._idx(ChamaInfernal)
    if idx is not None:
      self.idx_carta = idx
