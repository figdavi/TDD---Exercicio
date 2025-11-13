import pygame
from pathlib import Path
from snake.snake import Direction
from snake.game import Game

# Get graphics folder path
GRAPHICS_DIR = Path(__file__).resolve().parent / "graphics"

# Constants
DIMENSIONS = (640, 640)
dir_map: dict[int, Direction] = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
}

# Game initilization
game = Game(DIMENSIONS[0], DIMENSIONS[1])
pygame.init()
screen = pygame.display.set_mode((DIMENSIONS[0], DIMENSIONS[1]))
clock = pygame.time.Clock()

# Sprites
snake_head_img = pygame.image.load(GRAPHICS_DIR / "head_up.png").convert_alpha()
snake_body_img = pygame.image.load(GRAPHICS_DIR / "body_vertical.png").convert_alpha()
fruit_img = pygame.image.load(GRAPHICS_DIR / "apple.png").convert_alpha()

running = True
while running:
    screen.fill((0, 0, 0))

    # Quit button and key pressing logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in dir_map:
                game.snake.change_direction(new_direction=dir_map[event.key])

    # Move snake
    if not game.snake.move(game.height, game.width, game.fruits):
        print("Game Over")
        break
    game.spawn_fruits()

    # Snake drawing
    screen.blit(snake_head_img, game.snake.head)
    for x, y in game.snake.body:
        screen.blit(snake_body_img, (x, y))

    # Fruit drawing
    for x, y in game.fruits:
        screen.blit(fruit_img, (x, y))

    pygame.display.flip()
    clock.tick(60)

print("Quitting..")
pygame.quit()
