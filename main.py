import pygame
import sys

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS
from constants import ASTEROID_SPAWN_RATE_SECONDS
from constants import ASTEROID_MAX_RADIUS
from player import Player
from shot import Shot
from asteroid import Asteroid
from logger import log_state
from asteroidfield import AsteroidField
from logger import log_event


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable) # type: ignore
    Shot.containers = (shots, updatable, drawable) # type: ignore

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.Surface.fill(screen, (0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()


        clock.tick(60)
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
