# Documentação

```text
sage_card_captor/
│
├── main.py (motor do sistema)
├── settings.py (configs gerais)
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── src/ (código principal)
│   ├── __init__.py
│   │
│   ├── game.py (lançador do jogo)
│   ├── player.py
│   ├── enemys.py (classe de inimigo genérico)
│   ├── levels.py (carregador do mapa)
│   ├── ui.py (telas do jogo. start, config, inventário)
│   │
│   ├── systems/
│   │   ├── collision.py
│   │   ├── battle.py (mecânicas de batalha, efeito nos participantes, empilhamento de cartas)
│   │   └── purchase.py (loja, sistema de compra)
│   │
│   └── utils/
│       ├── helpers.py (tutoriais, balões de informação)
│       └── loader.py (tela de carregamento)
│
├── data/
│   ├── levels.json
│   ├── save.json
│
└── README.md
```
