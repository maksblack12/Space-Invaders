import pygame
from settings import *
from random import randint


class MrAlien:
    globalSpeed = -ALIEN_SPEED

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True
        self.nextShotDelay = pygame.time.get_ticks()+randint(ALIEN_MIN_DELAY, ALIEN_MAX_DELAY)

    def position(self):
        return (self.x, self.y)

    def hit(self, bullet_x, bullet_y):
        if self.x < bullet_x < self.x+ALIEN_SIZE[0] and self.y < bullet_y < self.y+ALIEN_SIZE[1]:
            self.isAlive = False
            return True
        return False

    def updatePosition(self):
        self.x += MrAlien.globalSpeed

    def isShotPossible(self):
        if pygame.time.get_ticks() >= self.nextShotDelay:
            self.nextShotDelay = pygame.time.get_ticks()+randint(ALIEN_MIN_DELAY, ALIEN_MAX_DELAY)
            return True
