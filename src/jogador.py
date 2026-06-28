# arquivo jogador modificado para a biblioteca pygame - teste

import pygame
from .cartas import criar_deck


class Personagem(pygame.sprite.Sprite):  # Agora herda de pygame.sprite.Sprite
  HP_MAX = 100
  SPEED_BASE = 50

  def __init__(self, nome, x, y):  # Adicionados x e y para posição na tela
    super().__init__()  # Inicializa os recursos do Sprite no Pygame

    # --- Atributos Visuais do Pygame ---
    # Cria um "corpo" visual temporário para o personagem
    self.image = pygame.Surface((50, 80))
    self.image.fill((0, 128, 255))  # Preenche com a cor azul
    self.rect = self.image.get_rect()  # Pega as dimensões para colisão/movimento
    self.rect.topleft = (x, y)  # Define a posição inicial na tela

    # --- Atributos Lógicos Originais ---
    # construtor que é chamado automaticamente quando um novo personagem é criado determinando seus atributos
    self.nome = nome
    self.hp = self.HP_MAX
    self.speed = self.SPEED_BASE
    self.defesa_atual = 0
    self.efeitos = []
    self.usos_fogo = 0
    self.deck = criar_deck()
    self.idx_carta = 0

  # propriedades
  @property
  def vivo(self):  # define se o personagem está sim ou não vivo
    return self.hp > 0

  @property
  def carta_atual(
    self,
  ):  # Usa o índice idx_carta para buscar e retornar a carta que está atualmente selecionada na lista self.deck
    if not self.deck:
      return None
    return self.deck[self.idx_carta]

  @property
  def hp_pct(
    self,
  ):  # Calcula a porcentagem de vida atual dividindo o HP atual pelo HP Máximo
    return self.hp / self.HP_MAX

  # ações
  def receber_dano(
    self, dano
  ):  # recebe o dano e impede que o numerador da vida desça abaixo de zero
    self.hp = max(0, self.hp - dano)

  def curar(
    self, valor
  ):  # cura o personagem e impede que a vida ultrapasse o máximo estabelecido
    antes = self.hp
    self.hp = min(self.HP_MAX, self.hp + valor)
    return self.hp - antes

  def proxima_carta(
    self,
  ):  # move a carta um indice a mais e se chegar no final do deck volta para a primeira carta do deck
    if self.deck:
      self.idx_carta = (self.idx_carta + 1) % len(self.deck)

  def carta_anterior(
    self,
  ):  # move a carta um indice a menos e se chegar no começo do deck volta para a ultima carta do deck
    if self.deck:
      self.idx_carta = (self.idx_carta - 1) % len(self.deck)

  def processar_efeitos(
    self,
  ):  # Percorre todos os efeitos de status aplicados ao personagem
    msgs = []
    vivos = []
    for e in self.efeitos:
      msgs.append(e.aplicar(self))  # aplica o uso dos efeitos
      if e.tick():  # diminui a quantidade de turnos ativos do efeito ao final da aplicação do efeito
        vivos.append(e)
    self.efeitos = vivos
    return msgs

  def status_str(self):
    if not self.efeitos:
      return "—"
    return ", ".join(
      f"{e.nome}({e.duracao})" for e in self.efeitos
    )  # Retorna um texto formatado mostrando os efeitos ativos e suas durações

  # --- Métodos extras para o Pygame ---
  def update(self):
    # Método padrão do Pygame que roda todo frame.
    # Aqui você pode colocar animações ou lógica que precisa ser verificada constantemente (ex: se hp <= 0, mudar imagem para morto).
    if not self.vivo:
      self.image.fill((100, 100, 100))  # Fica cinza se morrer

  def desenhar_interface(self, tela, fonte):
    """
    Usa as propriedades que você criou para desenhar informações na tela.
    """
    # 1. Desenha o nome do personagem acima dele
    texto_nome = fonte.render(self.nome, True, (255, 255, 255))
    tela.blit(texto_nome, (self.rect.x, self.rect.y - 25))

    # 2. Desenha a Barra de Vida usando a sua propriedade hp_pct
    largura_barra = 50
    altura_barra = 10
    cor_hp = (
      (0, 255, 0) if self.hp_pct > 0.3 else (255, 0, 0)
    )  # Fica vermelho se vida estiver baixa

    pygame.draw.rect(
      tela, (255, 0, 0), (self.rect.x, self.rect.y - 40, largura_barra, altura_barra)
    )  # Fundo vermelho
    pygame.draw.rect(
      tela,
      cor_hp,
      (self.rect.x, self.rect.y - 40, largura_barra * self.hp_pct, altura_barra),
    )  # Vida atual

    # 3. Desenha os Status (Veneno, etc)
    texto_status = fonte.render(self.status_str(), True, (255, 255, 0))
    tela.blit(texto_status, (self.rect.x, self.rect.bottom + 10))
