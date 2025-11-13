# O jogo deve também deve permitir que a cobra dê a volta na tela e quando a cobra atinge tamanho 10, duas frutas devem aparecer por vez, quando atingir 20, três frutas, e assim por diante.

from snake.snake import Snake
import random


class Game:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.snake: Snake = Snake(head=(width // 2, height // 2), body=[])
        self.fruits: list[tuple[int, int]] = []
        self.spawn_fruits()

    def required_fruit_count(self) -> int:
        return 1 + (len(self.snake.body) + 1) // 10

    def spawn_fruits(self):
        while len(self.fruits) < self.required_fruit_count():
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            new_fruit = (x, y)
            if (
                new_fruit not in self.snake.body
                and new_fruit != self.snake.head
                and new_fruit not in self.fruits
            ):
                self.fruits.append(new_fruit)
