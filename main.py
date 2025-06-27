import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 # Center of the screen
    player = Player(x, y)

    clock = pygame.time.Clock()  # Stores clock object in a variable
    dt = 0 # Delta time

    while True:
        Fill(screen, (0, 0, 0))  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 # Gets the time since the last frame in seconds

def Fill(screen, color): # Fills the screen with the specified colour
    screen.fill(color)

if __name__ == "__main__":
    main()
