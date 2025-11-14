import pygame
from pathlib import Path
from snake.snake import Direction
from snake.game import Game

# Constants
CLOCK_TICK_SPEED = 10
CELL_SIZE = 20
GRID_WIDTH = 512 // CELL_SIZE
GRID_HEIGHT = 512 // CELL_SIZE
DIMENSIONS = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
dir_map: dict[int, Direction] = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
}

# Game initilization
game = Game(GRID_WIDTH, GRID_HEIGHT)
pygame.init()
screen = pygame.display.set_mode((DIMENSIONS[0], DIMENSIONS[1]))
clock = pygame.time.Clock()

# Graphics directory containing all images
GRAPHICS_DIR = Path(__file__).resolve().parent / "graphics"

snake_body_img = pygame.image.load(GRAPHICS_DIR / "body_vertical.png").convert_alpha()
snake_body_img = pygame.transform.scale(snake_body_img, (CELL_SIZE, CELL_SIZE))
fruit_img = pygame.image.load(GRAPHICS_DIR / "apple.png").convert_alpha()
fruit_img = pygame.transform.scale(fruit_img, (CELL_SIZE, CELL_SIZE))


def load_all_images() -> dict[str, pygame.Surface]:
    images: dict[str, pygame.Surface] = {}
    for path in GRAPHICS_DIR.glob("*.png"):
        key = path.stem  # filename without extension
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        images[key] = img
    return images


images = load_all_images()


def get_head_img():
    img_name = "head_" + game.snake.direction
    return images[img_name]


running = True
while running:
    dir_changed_in_this_frame = False
    screen.fill((0, 0, 0))

    # Quit button and key pressing logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in dir_map and not dir_changed_in_this_frame:
                old_dir = game.snake.direction
                game.snake.change_direction(new_direction=dir_map[event.key])

                if game.snake.direction != old_dir:
                    dir_changed_in_this_frame = True

    # Move snake
    if not game.snake.move(game.height, game.width, game.fruits):
        print("Game Over")
        break
    game.spawn_fruits()

    # Snake drawing
    screen.blit(
        get_head_img(), (game.snake.head[0] * CELL_SIZE, game.snake.head[1] * CELL_SIZE)
    )
    for x, y in game.snake.body:
        screen.blit(snake_body_img, (x * CELL_SIZE, y * CELL_SIZE))

    # Fruit drawing
    for x, y in game.fruits:
        screen.blit(fruit_img, (x * CELL_SIZE, y * CELL_SIZE))

    pygame.display.flip()
    clock.tick(CLOCK_TICK_SPEED)

pygame.quit()
