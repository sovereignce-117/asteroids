import pygame
import random
from circleshape import *
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)

            new_vector1 = self.velocity.rotate(new_angle)
            new_vector2 = self.velocity.rotate(new_angle - (new_angle * 2))

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_vector1 * 1.2

            new_asteroid2 = Asteroid(self.position.x, self.position.y , new_radius)
            new_asteroid2.velocity = new_vector2 * 1.2