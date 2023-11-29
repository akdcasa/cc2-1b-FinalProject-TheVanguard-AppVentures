import pygame
import random

# Constants
WIDTH = 1920
HEIGHT = 1080
CELL_SIZE = 40
MAP_WIDTH = WIDTH // CELL_SIZE
MAP_HEIGHT = HEIGHT // CELL_SIZE
PLAYER_COLOR = (255, 255, 255)
OBSTACLE_COLOR = (128, 128, 128)

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            if not map[new_y][new_x]:
                self.x = new_x
                self.y = new_y

    def draw(self, surface):
        font = pygame.font.Font(None, CELL_SIZE)
        text = font.render("@", True, PLAYER_COLOR)
        surface.blit(text, (self.x * CELL_SIZE, self.y * CELL_SIZE))

# Generate a random map
def generate_map():
    map = [[False] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if random.random() < 0.2:  # 20% chance of obstacle
                map[y][x] = True
    return map

# Draw the map
def draw_map(surface):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map[y][x]:
                font = pygame.font.Font(None, CELL_SIZE)
                text = font.render("X", True, OBSTACLE_COLOR)
                surface.blit(text, (x * CELL_SIZE, y * CELL_SIZE))

# Main game loop
def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1))
    global map
    map = generate_map()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move(0, -1)
        elif keys[pygame.K_a]:
            player.move(-1, 0)
        elif keys[pygame.K_s]:
            player.move(0, 1)
        elif keys[pygame.K_d]:
            player.move(1, 0)

        screen.fill((0, 0, 0))
        draw_map(screen)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(10)

# Start the game
game_loop()
