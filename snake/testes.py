import pytest
from .snake import Snake


@pytest.fixture
def snake():
    return Snake(head=(0, 0), body=[(0, 0)])


def test_constructor(snake: Snake):
    assert snake.head == (0, 0)
    assert snake.body == [(0, 0)]
    assert snake.direction == "up"


def test_snake_moves_up(snake: Snake):
    snake.head = (2, 2)
    snake.body = [(2, 2)]
    snake.change_direction("up")

    snake.move()
    assert snake.direction == "up"
    assert snake.head == (2, 1)
    assert snake.body == [(2, 1)]


def test_snake_moves_down(snake: Snake):
    snake.head = (2, 2)
    snake.body = [(2, 2)]
    snake.direction = "left"  # start with safe direction
    snake.change_direction("down")

    snake.move()
    assert snake.direction == "down"
    assert snake.head == (2, 3)
    assert snake.body == [(2, 3)]


def test_snake_moves_left(snake: Snake):
    snake.head = (2, 2)
    snake.body = [(2, 2)]
    snake.change_direction("left")

    snake.move()
    assert snake.direction == "left"
    assert snake.head == (1, 2)
    assert snake.body == [(1, 2)]


def test_snake_moves_right(snake: Snake):
    snake.head = (2, 2)
    snake.body = [(2, 2)]
    snake.change_direction("right")

    snake.move()
    assert snake.direction == "right"
    assert snake.head == (3, 2)
    assert snake.body == [(3, 2)]


def test_snake_invalid_direction(snake: Snake):
    snake.change_direction("right")

    snake.change_direction("a")  # type: ignore
    snake.change_direction("lef")  # type: ignore

    assert snake.direction == "right"


def test_snake_cannot_reverse_direction(snake: Snake):
    snake.change_direction("left")
    snake.change_direction("right")
    assert snake.direction == "left"

    snake.change_direction("up")
    snake.change_direction("down")
    assert snake.direction == "up"


def test_snake_grows_when_eating_fruit(snake: Snake):
    snake.head = (2, 2)
    snake.body = [(2, 2)]
    snake.fruits.append((2, 1))
    snake.move()
    assert len(snake.body) == 2
