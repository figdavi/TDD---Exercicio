import pygame
from pathlib import Path
from snake.snake import Direction
from snake.game import Game

# Criar o caminho do arquivo de input e output
GRAPHICS_DIR = Path(__file__).resolve().parent / "graphics"

DIMENSIONS = (640, 640)
dir_map: dict[int, Direction] = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
}

game = Game(DIMENSIONS[0], DIMENSIONS[1])
pygame.init()
screen = pygame.display.set_mode((DIMENSIONS[0], DIMENSIONS[1]))

snake_head_img = pygame.image.load(GRAPHICS_DIR / "head_up.png").convert()
snake_body_img = pygame.image.load(GRAPHICS_DIR / "body_vertical.png").convert()

running = True
while running:
    # Quit button and key pressing logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in dir_map:
                game.snake.change_direction(new_direction=dir_map[event.key])

    # Snake drawing
    screen.blit(snake_head_img, game.snake.head)

    for x, y in game.snake.body:
        screen.blit(snake_body_img, (x, y))

    pygame.display.flip()

print("Quitting..")
pygame.quit()
