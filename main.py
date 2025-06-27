import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        Fill(screen, (0, 0, 0))  # Fill the screen with black
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

def Fill(screen, color):
    # Fills the screen with the specified color
    screen.fill(color)

if __name__ == "__main__":
    main()
