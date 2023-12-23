"""Game of Life"""
import sys
import pygame

# Dimensions
WIDTH, HEIGHT = 1000, 1000
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (240, 0, 0)
BLUE = (0, 0, 240)
CYAN = (0, 240, 240)
GREEN = (0, 240, 0)
YELLOW = (240, 240, 0)
ORANGE = (240, 160, 0)
PURPLE = (160, 0, 240)


class Game:
    """Represents a game"""
    def __init__(self):
        pass

    def draw(self, screen):
        """Draw the grid and the current objects"""


def main():
    """Runs the game"""
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Game object
    game = Game()

    while True:
        # Fill the background
        screen.fill(BLACK)

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
