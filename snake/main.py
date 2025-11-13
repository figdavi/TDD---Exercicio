import pygame
from snake.snake import Direction
from snake.game import Game

DIMENSIONS = (10, 15)
dir_map: dict[int, Direction] = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
}

game = Game(DIMENSIONS[0], DIMENSIONS[1])
pygame.init()
screen = pygame.display.set_mode((DIMENSIONS[0], DIMENSIONS[1]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in dir_map:
                game.snake.change_direction(new_direction=dir_map[event.key])

print("Quitting..")
pygame.quit()
