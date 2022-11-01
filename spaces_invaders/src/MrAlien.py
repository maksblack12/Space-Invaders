import pygame
from TheSettings import *
from random import randint


class MrAlien:
    runGuysRun = -ALIEN_SPEED

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True
        self.minDelay = 3000
        self.maxDelay = 5000
        self.meNextShot = pygame.time.get_ticks()+randint(self.minDelay, self.maxDelay)

    def coords(self):
        return (self.x, self.y)

    def hit(self, bullet_x, bullet_y):
        if self.x < bullet_x < self.x+100 and self.y < bullet_y < self.y+100:
            self.isAlive = False
            return True
        return False

    def runRunRun(self):
        self.x += MrAlien.runGuysRun

    def CanIPlsShoot(self):
        if pygame.time.get_ticks() >= self.meNextShot:
            self.meNextShot = pygame.time.get_ticks()+randint(self.minDelay, self.maxDelay)
            return True
