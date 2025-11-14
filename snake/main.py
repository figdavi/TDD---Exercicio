import pygame
from pathlib import Path
from snake.snake import Direction, Snake
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


loaded_images = load_all_images()


def get_head_img(snake: Snake):
    img_name = "head_" + snake.direction
    return loaded_images[img_name]


def get_body_img(snake: Snake, i: int):
    body = snake.body

    curr = body[i]

    # [head] [body0] [body1] ... [bodyn (or tail)]

    # segment behind the head
    if i == 0:
        prev_seg = snake.head
    else:
        prev_seg = body[i - 1]

    # last segment (tail)
    if i == len(body) - 1:
        next_seg = None
    else:
        next_seg = body[i + 1]

    cx, cy = curr
    px, py = prev_seg

    # If tail → determine orientation from prev_seg only
    if next_seg is None:
        # Tail orientation: where is prev_seg?
        if px == cx and py < cy:
            return "tail_down"
        if px == cx and py > cy:
            return "tail_up"
        if py == cy and px < cx:
            return "tail_right"
        if py == cy and px > cx:
            return "tail_left"

        return "tail_up"  # fallback

    nx, ny = next_seg

    # Straight pieces
    if px == nx:
        return "body_vertical"
    if py == ny:
        return "body_horizontal"

    # Corner pieces
    # turn top-left
    if (px < cx and ny < cy) or (nx < cx and py < cy):
        return "body_topleft"

    # turn bottom-left
    if (px < cx and ny > cy) or (nx < cx and py > cy):
        return "body_bottomleft"

    # turn top-right
    if (px > cx and ny < cy) or (nx > cx and py < cy):
        return "body_topright"

    # turn bottom-right
    if (px > cx and ny > cy) or (nx > cx and py > cy):
        return "body_bottomright"

    return "body_vertical"


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

                # Having more than one presses in one frame causes bugs (like unexpected Game Over)
                if game.snake.direction != old_dir:
                    dir_changed_in_this_frame = True

    # Move snake
    if not game.snake.move(game.height, game.width, game.fruits):
        print("Game Over")
        break
    game.spawn_fruits()

    # Snake drawing
    ## Head
    screen.blit(
        get_head_img(game.snake),
        (game.snake.head[0] * CELL_SIZE, game.snake.head[1] * CELL_SIZE),
    )

    ## Body (and tail)
    for i, body in enumerate(game.snake.body):
        x, y = body
        img_name = get_body_img(game.snake, i)
        img = loaded_images[img_name]
        screen.blit(img, (x * CELL_SIZE, y * CELL_SIZE))

    # Fruit drawing
    for x, y in game.fruits:
        screen.blit(fruit_img, (x * CELL_SIZE, y * CELL_SIZE))

    pygame.display.flip()
    clock.tick(CLOCK_TICK_SPEED)

pygame.quit()
