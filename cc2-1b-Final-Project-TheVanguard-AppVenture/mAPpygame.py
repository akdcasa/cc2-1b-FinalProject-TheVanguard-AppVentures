import pygame
import random

WIDTH = 1570
HEIGHT = 870
CELL_SIZE = 40
MAP_WIDTH = WIDTH // CELL_SIZE
MAP_HEIGHT = HEIGHT // CELL_SIZE
PLAYER_COLOR = (255, 255, 255)
OBSTACLE_COLOR = (128, 128, 128)
ENEMY_COLOR = (255, 0, 0)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            if not game_map[new_y][new_x]:
                self.x = new_x
                self.y = new_y

    def draw(self, surface):
        font = pygame.font.Font(None, CELL_SIZE)
        text = font.render("@", True, PLAYER_COLOR)
        surface.blit(text, (self.x * CELL_SIZE, self.y * CELL_SIZE))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_random(self):
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        dx, dy = random.choice(directions)
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            if not game_map[new_y][new_x]:
                self.x = new_x
                self.y = new_y

    def draw(self, surface):
        font = pygame.font.Font(None, CELL_SIZE)
        text = font.render("#", True, ENEMY_COLOR)
        surface.blit(text, (self.x * CELL_SIZE, self.y * CELL_SIZE))

def generate_map(width, height):
    game_map = [[False] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < 0.2:  # 20% chance of obstacle
                game_map[y][x] = True
    return game_map

def draw_map(surface, game_map, enemies):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if game_map[y][x]:
                font = pygame.font.Font(None, CELL_SIZE)
                text = font.render("X", True, OBSTACLE_COLOR)
                surface.blit(text, (x * CELL_SIZE, y * CELL_SIZE))

    for enemy in enemies:
        enemy.draw(surface)

# ...

# ...

# Main game loop
# Main game loop
def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1))
    global game_map  # Rename the global variable to game_map
    game_map = generate_map(MAP_WIDTH, MAP_HEIGHT)  # Assign the generated map to game_map
    enemies = [Enemy(random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)) for _ in range(3)]

    encounter_flag = False  # Flag to check if an encounter occurred

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

        for enemy in enemies:
            enemy.move_random()

        # Check for encounters with enemies
        for enemy in enemies:
            if player.x == enemy.x and player.y == enemy.y:
                print("Encountered an enemy!")
                encounter_flag = True


        # If an encounter occurred, exit the game loop
        if encounter_flag:
            pygame.quit()
            return

        # If an encounter occurred, exit the game loop
        if encounter_flag:
            pygame.quit()
            return

        screen.fill((0, 0, 0))
        draw_map(screen, game_map, enemies)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(10)

        if encounter_flag:
            # If an encounter occurred, exit the game loop
            pygame.quit()
            return

# Start the game
game_loop()
import randomenemyencounter
