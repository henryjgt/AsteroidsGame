"""Defines the asteroid sprite."""

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity


# class Asteroid(CircleShape):
#     def __init__(self, x, y, radius):
#         super().__init__(x, y, radius)

#     def draw(self, screen):
#         pygame.draw.circle(screen, "white", self.position, self.radius, 2)

#     def update(self, dt):
#         self.position += self.velocity * dt
