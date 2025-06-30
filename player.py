import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.timer = 0

    def triangle(self): # Returns the vertices of the triangle representing the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) # Draws the player as a triangle

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            return
        else:
            player_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            forward = player_direction * PLAYER_SHOT_SPEED
            shot_position = self.position + (player_direction * self.radius)  # Position the shot at the front of the player
            shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS, forward) 
            self.timer += SHOT_RATE