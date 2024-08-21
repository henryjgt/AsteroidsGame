#! usr/bin/env python3.12

"""An implementation of the classic arcade game 'Asteroids'."""

import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    clock = pygame.time.Clock()
    centre_x = 0.5 * SCREEN_WIDTH
    centre_y = 0.5 * SCREEN_HEIGHT
    player = Player(centre_x, centre_y)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0, 0, 0), rect=None)
        player.draw(screen)
        pygame.display.flip()

        delta = clock.tick(60)
        dt = 0.001 * delta


if __name__ == "__main__":
    main()
