from settings import *

class Bullet:
    def __init__(self, x, y, wasFiredFromShip):
        self.x = x
        self.y = y
        self.isAlive=True
        self.wasFiredFromShip = wasFiredFromShip

    def update(self, aliens, theBoss, player):
        if self.wasFiredFromShip:
            self.y -= BULLET_SPEED
        else:
            self.y += BULLET_SPEED
        if self.wasFiredFromShip:
            for alien in aliens:
                if alien.hit(self.x, self.y):
                    self.isAlive = False
            if theBoss.damage(self.x, self.y):
                self.isAlive = False
            if self.y < 0:
                self.isAlive = False
        else:
            if player.wasHit(self.x, self.y):
                self.isAlive = False
            if self.y > SCREEN_H:
                self.isAlive = False

    def draw(self, screen, bullet_img, theBoss, aliens_bullet_img, boss_bullet_img):
        if not self.wasFiredFromShip:
            if theBoss.isAlive == False:
                screen.blit(aliens_bullet_img, (self.x, self.y))
            else:
                screen.blit(boss_bullet_img, (self.x, self.y))
        else:
            screen.blit(bullet_img, (self.x, self.y))
