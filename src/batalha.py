# arquivo de batalha em pygame - teste

from .jogador import Personagem
from .inimigos import CPU
import pygame
import sys

_ESPERA = "espera"
_ANIMANDO = "animando"
_FIM = "fim"


class Batalha:
  LOG_MAX = 7  # quantidade maxima de mensagens na tela
  DELAY_FPS = 38  # Cria um intervalo de tempo, medido em quadros (frames), entre as ações automáticas de um turno.

  def __init__(self, nome_jogador):
    self.jogador = Personagem(nome_jogador, x=300, y=450)
    self.cpu = CPU(nome="Computador", x=1500, y=450)
    self.log = ["⚔️  Batalha iniciada!", "Escolha sua carta e pressione ENTER."]
    self.turno = 1
    self.resultado = None
    self._estado = _ESPERA
    self._fila = []
    self._timer = 0

  @property
  def aguardando_input(self):
    return self._estado == _ESPERA

  @property
  def encerrada(self):
    return self._estado == _FIM

  def input(self, acao):
    if self._estado != _ESPERA:
      return
    if acao == "esquerda":
      self.jogador.carta_anterior()
    elif acao == "direita":
      self.jogador.proxima_carta()
    elif acao == "usar":
      self._montar_turno()

  def tick(self):
    if self._estado != _ANIMANDO:
      return
    self._timer -= 1
    if self._timer <= 0:
      self._executar_proxima()

  # montagem do turno
  def _montar_turno(self):
    self.jogador.defesa_atual = 0
    self.cpu.defesa_atual = 0
    self._fila = [
      ("jogador_usa", self.jogador, self.cpu),
      ("cpu_escolhe", None, None),
      ("cpu_usa", self.cpu, self.jogador),
      ("efeitos", self.jogador, None),
      ("efeitos", self.cpu, None),
      ("fim_turno", None, None),
    ]
    self._estado = _ANIMANDO
    self._executar_proxima()

  def _executar_proxima(self):
    if not self._fila:
      return

    tipo, sujeito, alvo = self._fila.pop(0)
    estado_acao = {}

    if tipo == "jogador_usa":
      msg, _ = sujeito.carta_atual.usar(sujeito, alvo, estado_acao)
      self._log(msg)
      if estado_acao.get("fugiu"):
        self._encerrar("fuga")
        return

    elif tipo == "cpu_escolhe":
      self.cpu.escolher_carta()

    elif tipo == "cpu_usa":
      msg, _ = sujeito.carta_atual.usar(sujeito, alvo, estado_acao)
      self._log(msg)
      self.cpu.ultima_carta_usada = sujeito.carta_atual

    elif tipo == "efeitos":
      for msg in sujeito.processar_efeitos():
        self._log(msg)

    elif tipo == "fim_turno":
      self.turno += 1
      if not self.jogador.vivo:
        self._encerrar("derrota")
        return
      if not self.cpu.vivo:
        self._encerrar("vitoria")
        return
      self._fila.clear()
      self._estado = _ESPERA
      return

    # Verifica morte imediata
    if tipo in ("jogador_usa", "cpu_usa", "efeitos"):
      if not self.jogador.vivo:
        self._encerrar("derrota")
        return
      if not self.cpu.vivo:
        self._encerrar("vitoria")
        return

    self._timer = self.DELAY_FPS if self._fila else 0
    if not self._fila:
      self._estado = _ESPERA

  def _encerrar(self, resultado):
    self.resultado = resultado
    self._log(
      {
        "vitoria": "✦ VITÓRIA! Você derrotou o Chefão! ✦",
        "derrota": "✦ DERROTA! O Chefão venceu... ✦",
        "fuga": "✦ Você fugiu da batalha. ✦",
      }[resultado]
    )
    self._estado = _FIM

  def _log(self, msg):
    self.log.append(msg)
    if len(self.log) > self.LOG_MAX:
      self.log.pop(0)


# CÓDIGO DE INTEGRAÇÃO COM O PYGAME


def iniciar_jogo(game):
  pygame.display.set_caption("Batalha de Cartas")
  tela = game._screen
  ALTURA, LARGURA = tela.size
  # Controle de FPS (Frames Por Segundo)
  relogio = pygame.time.Clock()
  FPS = 60  # O DELAY_FPS 38 vai demorar aprox. 0.6 segundos visualmente

  # Fontes e Cores
  # Tenta usar a Segoe UI Emoji se estiver no Windows para renderizar o emoji da espada "⚔️"
  fonte_log = pygame.font.Font("assets/fonts/segoe-ui-emoji.ttf", 28)

  COR_FUNDO = (30, 30, 40)
  COR_TEXTO = (220, 220, 220)
  COR_DESTAQUE = (255, 215, 0)

  # Instancia a Batalha
  batalha = Batalha("Heroi")

  rodando = True
  while rodando:
    # PROCESSAMENTO DE EVENTOS (Inputs)
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        rodando = False
        continue

      # Captura de teclas de ação
      if evento.type == pygame.KEYDOWN:
        # O jogador só consegue agir se a batalha estiver esperando input
        if evento.key == pygame.K_f:
          game.resize()
        if evento.key == pygame.K_ESCAPE:
          rodando = False
          continue
        if batalha.aguardando_input:
          if (evento.key == pygame.K_LEFT) or (evento.key == pygame.K_a):
            batalha.input("esquerda")
          elif (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_d):
            batalha.input("direita")
          elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
            batalha.input("usar")

    # 2. ATUALIZAÇÃO DA LÓGICA (Tick)
    batalha.tick()

    # 3. RENDERIZAÇÃO
    tela.fill(COR_FUNDO)

    # CONTEÚDO VISUAL (Personagens e Cartas)

    # retângulos coloridos do Jogador e da CPU nas suas posições
    tela.blit(batalha.jogador.image, batalha.jogador.rect)
    tela.blit(batalha.cpu.image, batalha.cpu.rect)

    #  nomes e as barras de vida
    batalha.jogador.desenhar_interface(tela, fonte_log)
    batalha.cpu.desenhar_interface(tela, fonte_log)

    #  Desenha a Mão de Cartas
    if batalha.aguardando_input and batalha.jogador.deck:
      total_cartas = len(batalha.jogador.deck)
      largura_carta = tela.width * 0.9 / total_cartas
      espacamento = largura_carta * 0.9

      # Calcula o tamanho total da mão para centralizar
      x_inicial = LARGURA

      # Coordenadas Y ajustadas para ̶̶1̶̶̶0̶̶̶8̶̶̶0̶̶̶p o tamanho da tela
      y_base = ALTURA - 250  # Cartas normais ficam na base da tela
      y_selecionada = y_base - 100  # Carta selecionada "pula" para cima

      # Desenha todas as cartas NÃO selecionadas primeiro
      for i, carta in enumerate(batalha.jogador.deck):
        if i != batalha.jogador.idx_carta:
          carta.rect.x = x_inicial + (i * espacamento)
          carta.rect.y = y_base
          carta.desenhar(tela, fonte_log, fonte_log)

      # Desenhar a carta SELECIONADA por último (por cima)
      carta_atual = batalha.jogador.carta_atual
      carta_atual.rect.x = x_inicial + (batalha.jogador.idx_carta * espacamento)
      carta_atual.rect.y = y_selecionada

      # Desenhar a carta atual destacada
      carta_atual.desenhar(tela, fonte_log, fonte_log)

      # Desenhar o contorno brilhante
      pygame.draw.rect(tela, COR_DESTAQUE, carta_atual.rect, 3)

    # TEXTOS DE INTERFACE E LOGS

    # Desenhar o turno atual
    texto_turno = fonte_log.render(f"Turno: {batalha.turno}", True, COR_DESTAQUE)
    tela.blit(texto_turno, (720, 40))

    # Indicador de estado para o jogador
    if batalha.aguardando_input:
      texto_estado = fonte_log.render(
        "Sua vez! (Setas para escolher, ENTER para usar)", True, (100, 255, 100)
      )
    elif batalha.encerrada:
      texto_estado = fonte_log.render("Pressione ESC para sair", True, (255, 100, 100))
      # Permite fechar após o fim da partida
      teclas = pygame.key.get_pressed()
      if teclas[pygame.K_ESCAPE]:
        rodando = False
    else:
      texto_estado = fonte_log.render("Aguarde...", True, (200, 200, 200))
    tela.blit(texto_estado, (20, 50))

    # Desenhar os Logs da batalha
    y_offset = 100
    for i, msg in enumerate(batalha.log):
      opacidade = 255 if i == len(batalha.log) - 1 else 180
      surface_texto = fonte_log.render(msg, True, COR_TEXTO)
      surface_texto.set_alpha(opacidade)
      tela.blit(surface_texto, (720, y_offset))
      y_offset += 35

    # Atualiza a janela
    pygame.display.flip()

    # Trava o loop em 60 FPS
    relogio.tick(FPS)
