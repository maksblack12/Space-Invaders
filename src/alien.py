import pygame
from settings import *
from bullet import *
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

    def update(self, aliens_attack):
        self.x += MrAlien.globalSpeed
        if self.x <= 0:
            MrAlien.globalSpeed = ALIEN_SPEED
        if self.x >= SCREEN_W-100:
            MrAlien.globalSpeed = - ALIEN_SPEED

        if pygame.time.get_ticks() >= self.nextShotDelay:
            self.nextShotDelay = pygame.time.get_ticks()+randint(ALIEN_MIN_DELAY, ALIEN_MAX_DELAY)
            aliens_attack.append(Bullet(self.x+45, self.y+55, False))

