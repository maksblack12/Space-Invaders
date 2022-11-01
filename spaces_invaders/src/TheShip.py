import pygame
from TheSettings import *
from TheBoss import *

theBoss=TheBoss()

class TheShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = SHIP_SPEED
        self.yer_last_shot_capin = pygame.time.get_ticks()
        self.last_laser = pygame.time.get_ticks()
        self.last_shield = pygame.time.get_ticks()
        self.bullet_delay = 300
        self.laser_delay = 1000
        self.maxHp = 20
        self.Hp = self.maxHp

    def move_left(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x >= SCREEN_W-100:
            self.x = SCREEN_W-100

    def CouldIShoot(self):
        if pygame.time.get_ticks()-self.yer_last_shot_capin >= self.bullet_delay:
            self.yer_last_shot_capin = pygame.time.get_ticks()
            return True
        return False

    def Laser(self):
        if pygame.time.get_ticks()-self.last_laser >= self.laser_delay:
            self.last_laser = pygame.time.get_ticks()
            return True
        return False

    def Shield(self):
        if pygame.time.get_ticks()-self.last_shield >= self.shield_delay:
            self.last_shield = pygame.time.get_ticks()
            return True
        return False

    def hit(self, bullet_x, bullet_y):
        if self.x < bullet_x < self.x+100 and self.y < bullet_y < self.y+100:
            with open("src/bossAlive.txt", "r") as file:
                if file.read()=="True":
                    self.Hp-=2
                else:
                    self.Hp -= 1
            return True
        return False

    def myHealthStatus(self):
        return f"{self.Hp}/{self.maxHp}"


    def TheCoords(self):
        return (self.x, self.y)

    def laser_r(self):
        return self.laser_ready
