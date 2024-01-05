"""Game of Life"""
import sys
import pygame
from entities import Cell
from presets import (
    GLIDER,
    GOSPER_GUN,
)
from constants import (
    WIDTH,
    HEIGHT,
    GRID_SIZE,
    GRAY,
    LIGHTGRAY,
    WHITE,
    BLACK,
)


class Game:
    """Represents a game"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []

    def update(self):
        """Update the cells in the game"""
        cell_positions, empty_positions = self.positions_to_check()
        births, deaths = set(), set()
        for x, y in cell_positions:
            count = 0
            for neighbor in self.get_neighbors(x, y):
                if neighbor in cell_positions:
                    count += 1
            if count <= 1 or count >= 4:
                deaths.add((x, y))
        for x, y in empty_positions:
            count = 0
            for neighbor in self.get_neighbors(x, y):
                if neighbor in cell_positions:
                    count += 1
            if count == 3:
                births.add((x, y))
        for cell in self.cells.copy():
            position = cell.get_pos()
            if position in deaths:
                self.cells.remove(cell)
        for x, y in births:
            self.cells.append(Cell(x, y, GRID_SIZE, WHITE))

    def add_cell(self, x, y):
        """Add a new cell"""
        self.cells.append(Cell(x, y, GRID_SIZE, WHITE))

    def del_cell(self, x, y):
        """Remove a cell if it exists"""
        to_remove = None
        for i, cell in enumerate(self.cells):
            if (x, y) == cell.get_pos():
                to_remove = i
        if to_remove is not None:
            self.cells.remove(self.cells[to_remove])
            return True
        return False

    def add_preset(self, preset):
        """Adds cells of a preset"""
        min_x, max_x = min(preset)[0], max(preset)[0]
        min_y, max_y = min(preset)[1], max(preset)[1]
        avg_x, avg_y = (max_x - min_x) // 2, (max_y - min_y) // 2
        dx = (WIDTH // GRID_SIZE) // 2 - avg_x
        dy = (HEIGHT // GRID_SIZE) // 2 - avg_y
        for x, y in preset:
            print(x + dx,  y + dy)
            self.add_cell(x + dx, y + dy)

    def is_cell(self, x, y):
        """Checks if a cell already exists"""
        for cell in self.cells:
            if (x, y) == cell.get_pos():
                return True
        return False

    def draw(self, screen):
        """Draw the current game objects"""
        for cell in self.cells:
            draw_rect(screen, cell)

    def in_bounds(self, x, y):
        """Checks if a position is not out of bounds"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        return False

    def get_neighbors(self, x, y):
        """Get positions of neighboring spaces"""
        neighbors = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if self.in_bounds(dx + x, dy + y):
                    neighbors.add((dx + x, dy + y))
        return neighbors

    def positions_to_check(self):
        """Returns all positions for rule checking"""
        cell_positions = set()
        for cell in self.cells:
            cell_positions.add((cell.x, cell.y))
        empty_positions = set()
        for x, y in cell_positions:
            for neighbor in self.get_neighbors(x, y):
                if neighbor not in cell_positions:
                    empty_positions.add(neighbor)
        return cell_positions, empty_positions


def draw_rect(screen, obj):
    """Draws a Pygame rectangle"""
    x, y, size = (obj.x * obj.size) + 1, (obj.y * obj.size) + 1, obj.size - 1
    pygame.draw.rect(screen, obj.color, (x, y, size, size))


def draw_grid(screen):
    """Draws a grid"""
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def main():
    """Initializes and runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

    fps = 10
    selecting = True

    # Fill the background
    screen.fill(BLACK)
    draw_grid(screen)
    pygame.display.update()
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    selecting = False
                if event.key == pygame.K_1:
                    game.add_preset(GLIDER)
                    game.draw(screen)
                    pygame.display.update()
                if event.key == pygame.K_2:
                    game.add_preset(GOSPER_GUN)
                    game.draw(screen)
                    pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                x = (x // GRID_SIZE) * GRID_SIZE
                y = (y // GRID_SIZE) * GRID_SIZE
                size = GRID_SIZE

                screen.fill(BLACK)
                draw_grid(screen)
                pygame.draw.rect(screen, LIGHTGRAY, (x, y, size, size))
                game.draw(screen)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // GRID_SIZE, y // GRID_SIZE
                if game.is_cell(x, y):
                    game.del_cell(x, y)
                else:
                    game.add_cell(x, y)
                game.draw(screen)
                pygame.display.update()

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pass
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pass
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass

        # Set the framerate
        clock.tick(60)

    while True:
        # Fill the background
        screen.fill(BLACK)
        draw_grid(screen)

        for event in pygame.event.get():
            # Check for the QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
            if event.type == pygame.KEYUP:
                pass

            # Check for the MOUSEBUTTONDOWN event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            fps = max((fps-1, 1))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            fps = min((fps+1, 60))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass

        # Draw the grid and current state
        game.draw(screen)
        # Update the game state
        game.update()
        # Update the display
        pygame.display.update()
        # Set the framerate
        clock.tick(fps)


if __name__ == "__main__":
    main()
