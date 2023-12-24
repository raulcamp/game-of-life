"""Game of Life"""
import sys
import pygame
from entities import Cell
from constants import (
    WIDTH,
    HEIGHT,
    GRID_SIZE,
    GRAY,
    WHITE,
    BLACK,
)


class Game:
    """Represents a game"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [  # TODO: add input for initialization cells
            Cell(self.width // 2, self.height // 2, GRID_SIZE, WHITE),
            Cell(self.width // 2 + 1, self.height // 2 + 1, GRID_SIZE, WHITE),
            Cell(self.width // 2 + 1, self.height // 2 + 2, GRID_SIZE, WHITE),
            Cell(self.width // 2, self.height // 2 + 2, GRID_SIZE, WHITE),
            Cell(self.width // 2 - 1, self.height // 2 + 2, GRID_SIZE, WHITE),
        ]

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
    """Runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

    fps = 10

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
                    fps = min((fps+1, 60))
                if event.key == pygame.K_LEFT:
                    fps = max((fps-1, 1))
            if event.type == pygame.KEYUP:
                pass

            # Check for the MOUSEBUTTONDOWN event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

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

        # Draw the grid and current state
        game.draw(screen)
        # Update the game state
        game.update()
        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(fps)


if __name__ == "__main__":
    main()
