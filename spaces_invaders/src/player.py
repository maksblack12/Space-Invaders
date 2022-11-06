import pygame
from settings import *

class Player:
    def __init__(self, x, y, boss):
        self.x = x
        self.y = y
        self.boss = boss
        self.bulletDelay = 300
        self.lastShotTime = pygame.time.get_ticks()+self.bulletDelay
        self.lastLaserTime = pygame.time.get_ticks()+PLAYER_LASER_DELAY
        self.maxHp = 20
        self.hasShield = False
        self.hp = self.maxHp

    def moveLeft(self):
        self.x -= SHIP_SPEED
        if self.x <= 0:
            self.x = 0

    def moveRight(self):
        self.x += SHIP_SPEED
        if self.x >= SCREEN_W-100:
            self.x = SCREEN_W-100

    def isShotPossible(self):
        if pygame.time.get_ticks()-self.lastShotTime >= self.bulletDelay:
            self.lastShotTime = pygame.time.get_ticks()
            return True
        return False

    def isLaserPossible(self):
        if pygame.time.get_ticks()-self.lastLaserTime >= PLAYER_LASER_DELAY:
            self.lastLaserTime = pygame.time.get_ticks()
            return True
        return False

    def wasHit(self, bullet_x, bullet_y):
        if self.x < bullet_x < self.x+100 and self.y < bullet_y < self.y+100:
            if self.hasShield:
                return False
            if (self.boss.isAlive):
                self.hp-=2
            else:
                self.hp -= 1
            return True

    def getHp(self):
        return f"{self.hp}/{self.maxHp}"


    def position(self):
        return (self.x, self.y)

