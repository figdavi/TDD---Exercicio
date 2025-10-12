import pytest
from .snake import Snake


@pytest.fixture
def snake():
    return Snake(head=(0, 0), body=[(0, 0)])


def test_constructor(snake: Snake):
    assert snake.head == (0, 0)
    assert snake.body == [(0, 0)]


def test_snake_moves_right(snake: Snake):
    snake.move("right")
    assert snake.head == (1, 0)
    assert snake.body == [(1, 0)]
