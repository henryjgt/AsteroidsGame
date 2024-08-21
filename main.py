#! usr/bin/env python3.12

"""An implementation of the classic arcade game 'Asteroids'."""

import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    CENTRE_X = 0.5 * SCREEN_WIDTH
    CENTRE_Y = 0.5 * SCREEN_HEIGHT

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    Player.containers = (drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(CENTRE_X, CENTRE_Y)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for uobj in updatable:
            uobj.update(dt)

        if any(asteroid.has_collided(player) for asteroid in asteroids):
            print("Game Over!")
            pygame.quit()
            sys.exit(0)

        screen.fill("black")

        for dobj in drawable:
            dobj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = 0.001 * clock.tick(60)


if __name__ == "__main__":
    main()
