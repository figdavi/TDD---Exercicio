import os
import keyboard
import time
from snake.game import Game


class io_handler:
    x_size: int
    y_size: int
    game_speed = float
    last_input: str
    matrix = []

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]

        self.game_speed = speed
        self.last_input = "w"

        for i in range(self.y_size):
            self.matrix.append([0] * self.x_size)

    def record_inputs(self):
        keyboard.add_hotkey("w", lambda: setattr(self, "last_input", "w"))
        keyboard.add_hotkey("a", lambda: setattr(self, "last_input", "a"))
        keyboard.add_hotkey("s", lambda: setattr(self, "last_input", "s"))
        keyboard.add_hotkey("d", lambda: setattr(self, "last_input", "d"))
        keyboard.add_hotkey("esc", lambda: setattr(self, "last_input", "end"))

    def display(self):
        def display_h_line(self):
            print("+", end="")
            print("--" * len(self.matrix[0]), end="")
            print("+")

        def display_content_line(line):
            print("|", end="")
            for item in line:
                if item == 1:
                    print("[]", end="")
                elif item == 2:
                    print("<>", end="")
                elif item == 3:
                    print("()", end="")
                else:
                    print("  ", end="")

            print("|")

        os.system("cls" if os.name == "nt" else "clear")
        display_h_line(self)
        for line in self.matrix:
            display_content_line(line)
        display_h_line(self)


instance = io_handler((10, 15), 0.5)
game = Game(10, 10)


def game_loop():
    instance.record_inputs()
    while True:
        instance.display()
        print("mova com WASD, saia com esc. Ultimo botão:", end=" ")
        dir_map = {"w": "up", "s": "down", "a": "left", "d": "right"}
        if instance.last_input in dir_map:
            game.snake.change_direction(dir_map[instance.last_input])

        # Move snake
        if not game.snake.move(game.height, game.width, game.fruits):
            print("Game Over")
            break
        game.spawn_fruits()

        update_matrix()

        print(instance.last_input)
        if instance.last_input == "end":
            exit()
        time.sleep(instance.game_speed)


def update_matrix():
    # Update matrix
    instance.matrix = [[0] * game.width for _ in range(game.height)]
    for x, y in game.snake.body:
        instance.matrix[y][x] = 1
    hx, hy = game.snake.head
    instance.matrix[hy][hx] = 2
    for fx, fy in game.fruits:
        instance.matrix[fy][fx] = 3


game_loop()
