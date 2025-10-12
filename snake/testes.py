import pytest
from .snake import Snake


@pytest.fixture
def snake():
    return Snake(start_pos=(0, 0))


def test_constructor(snake: Snake):
    assert snake.position == (0, 0)
