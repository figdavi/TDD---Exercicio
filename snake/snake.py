from typing import Literal

type Direction = Literal["up", "down", "right", "left"]


class Snake:
    def __init__(self, head: tuple[int, int], body: list[tuple[int, int]]):
        self.head = head
        self.body = body
        self.direction: Direction = "up"

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
        self.body.pop()
