from typing import Literal

Direction = Literal["up", "down", "right", "left"]


class Snake:
    def __init__(self, head: tuple[int, int], body: list[tuple[int, int]]):
        self.head = head
        self.body = body
        self.direction: Direction = "up"

    def move(self, height: int, width: int, fruits: list[tuple[int, int]]) -> bool:
        x, y = self.head
        match self.direction:
            # upmost is [0][0]
            case "up":
                y = (y - 1) % height
            case "down":
                y = (y + 1) % height
            case "left":
                x = (x - 1) % width
            case "right":
                x = (x + 1) % width

        new_head = (x, y)

        # Check if head movement will collide with body
        if new_head in self.body:
            return False

        self.head = new_head
        self.body.insert(0, self.head)

        # Fruit eating logic
        if self.head not in fruits:
            self.body.pop()
        else:
            fruits.remove(self.head)

        return True

    def change_direction(self, new_direction: Direction):
        # Checks if new_direction is a valid direction
        if new_direction not in Direction.__args__:
            print("Invalid direction.")
            return

        opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}

        if new_direction == opposite[self.direction]:
            return

        self.direction = new_direction
