#jogabilidade da luta do jogo de ip
class Carta:
    def _init_(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor


class Jogador:
    def _init_(self, nome):
        self.nome = nome
        self.vida = 100
        self.defesa = 0

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        self.defesa = 0
        return dano_final

    def curar(self, valor):
        self.vida = min(100, self.vida + valor)


class Batalha:
    def _init_(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def atacar(self, atacante, alvo, dano):
        dano_final = alvo.receber_dano(dano)
        print(
            f"{atacante.nome} causou "
            f"{dano_final} de dano em {alvo.nome}!"
        )

#cartas
golpe_rapido = Carta("Golpe Rápido", "ataque", 20)
corte_forte = Carta("Corte Forte", "ataque", 30)
ataque_supremo = Carta("Ataque Supremo", "ataque", 40)

escudo = Carta("Escudo", "defesa", 15)
barreira = Carta("Barreira", "defesa", 25)
defesa_total = Carta("Defesa Total", "defesa", 999)

cura_pequena = Carta("Cura Pequena", "cura", 20)
cura_grande = Carta("Cura Grande", "cura", 35)

fuga = Carta("Fuga", "especial", 0)


#jogador
jogador = Jogador("Renatiel")
cpu = Jogador("CPU")
batalha = Batalha(jogador, cpu)
