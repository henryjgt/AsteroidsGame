#! usr/bin/env python3.12

"""An implementation of the classic arcade game 'Asteroids'."""

import pygame

from constants import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0, 0, 0), rect=None)
        pygame.display.flip()


if __name__ == "__main__":
    main()
