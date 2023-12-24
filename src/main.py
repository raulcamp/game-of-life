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
            Cell(self.width // 2 + 1, self.height // 2, GRID_SIZE, WHITE),
            Cell(self.width // 2 + 1, self.height // 2 + 1, GRID_SIZE, WHITE),
            Cell(self.width // 2 - 1, self.height // 2 - 1, GRID_SIZE, WHITE),
        ]

    def draw(self, screen):
        """Draw the current game objects"""
        for cell in self.cells:
            draw_rect(screen, cell)


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
                pass
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
        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(60)


if __name__ == "__main__":
    main()
