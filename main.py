import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    shots = pygame.sprite.Group()  # Add a group to hold all shots
    asteroids = pygame.sprite.Group() # Add a group to hold all asteroids
    updateables = pygame.sprite.Group() # Add a group to hold all updateable objects
    drawables = pygame.sprite.Group() # Add a group to hold all drawable objects
    Shot.containers = (shots, updateables)
    Asteroid.containers = (asteroids, updateables, drawables) # Set the containers for the asteroid class
    Player.containers = (updateables, drawables) # Set the containers for the player class
    AsteroidField.containers = (updateables, ) # Set the containers for the asteroid field class

    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 # Center of the screen
    player = Player(x, y)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()  # Stores clock object in a variable
    dt = 0 # Delta time

    while True:
        dt = clock.tick(60) / 1000 # Gets the time since the last frame in seconds
        screen.fill((0, 0, 0))  # Fill the screen with black
        updateables.update(dt)
        for obj in drawables:
            obj.draw(screen)
        for shot in shots:
            shot.draw(screen)
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

def Fill(screen, color): # Fills the screen with the specified colour
    screen.fill(color)

if __name__ == "__main__":
    main()
