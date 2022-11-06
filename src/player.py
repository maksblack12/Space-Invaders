import pygame
from settings import *
from bullet import *

class Player:
    def __init__(self, x, y, boss):
        self.x = x
        self.y = y
        self.boss = boss
        self.bulletDelay = 300
        self.lastShotTime = pygame.time.get_ticks()+self.bulletDelay
        self.lastLaserTime = pygame.time.get_ticks()+PLAYER_LASER_DELAY
        self.lastShieldActive = pygame.time.get_ticks()+SHIP_SHIELD_DELAY
        self.shieldOnTimer = 0
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

    def updateShield(self,isKeyPressed):
        if self.hasShield:
            if pygame.time.get_ticks()-self.shieldOnTimer >= SHIP_SHIELD_TIME:
                self.lastShieldActive = pygame.time.get_ticks()
                self.hasShield = False
        else:
            if isKeyPressed and pygame.time.get_ticks()-self.lastShieldActive >= SHIP_SHIELD_DELAY:
                self.shieldOnTimer = pygame.time.get_ticks()
                self.hasShield=True

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

    def update(self, keys, bullets):
        if keys[pygame.K_a]:
            self.moveLeft()
        if keys[pygame.K_d]:
            self.moveRight()
        if keys[pygame.K_SPACE] and self.isShotPossible():
            bullets.append(Bullet(self.x+42, SCREEN_H-100, True))
        if keys[pygame.K_w] and self.isLaserPossible():
            for i in range(0, 5):
                bullets.append(Bullet(self.x+42, SCREEN_H-100-50*i, True))
        self.updateShield(keys[pygame.K_s])

    def draw(self, screen, imageManager):
        screen.blit(imageManager.get("player"), (self.x, self.y))
        if self.hasShield:
            screen.blit(imageManager.get("player_shield"), (self.x, self.y))

