import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # FPS Lock
    dt = 0
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)

    # create player
    player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))

    # create asteroids
    asteroidfield = AsteroidField()

    # game loop start
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        print(drawable)
        updatable.update(dt)

        # player collision check
        for a in asteroids:
            if a.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # shot collision check
        for c in asteroids:
            for s in shots:
                if c.collides_with(s) == True:
                    log_event("asteroid_shot")
                    c.split()
                    s.kill()

        for i in drawable:
            i.draw(screen)
        

        pygame.display.flip()
        # lock framerate to 60fps and log time between .tick calls
        time_passed = clock.tick(60)
        dt = time_passed / 1000
        
        
    


if __name__ == "__main__":
    main()
