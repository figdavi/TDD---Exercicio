# O jogo deve também deve permitir que a cobra dê a volta na tela e quando a cobra atinge tamanho 10, duas frutas devem aparecer por vez, quando atingir 20, três frutas, e assim por diante.

from .snake import Snake


class Game:
    def __init__(self, height: int, width: int, snake: Snake):
        self.height = height
        self.width = width
        self.snake = snake
        self.fruits: list[tuple[int, int]] = []
