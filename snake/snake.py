from typing import Literal

Direction = Literal["up", "down", "right", "left"]


class Snake:
    def __init__(self, head: tuple[int, int], body: list[tuple[int, int]]):
        self.head = head
        self.body = body
        self.direction: Direction = "up"
        self.fruits: list[tuple[int, int]] = []

    def move(self):
        x, y = self.head
        match self.direction:
            # upmost is [0][0]
            case "up":
                y -= 1
            case "down":
                y += 1
            case "left":
                x -= 1
            case "right":
                x += 1

        self.head = (x, y)
        self.body.insert(0, self.head)

        # Fruit eating logic
        if self.head not in self.fruits:
            self.body.pop()
        else:
            self.fruits.remove(self.head)

    def change_direction(self, new_direction: Direction):
        # Checks if new_direction is a valid direction
        if new_direction not in Direction.__args__:
            print("Invalid direction.")
            return

        opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}

        if new_direction == opposite[self.direction]:
            return

        self.direction = new_direction
