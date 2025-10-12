import pytest
from .snake import Snake


def test_constructor():
    snake = Snake(position=(0, 0))

    assert snake.position == (0, 0)
