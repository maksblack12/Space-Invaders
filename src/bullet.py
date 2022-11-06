from settings import *

class Bullet:
    def __init__(self, x, y, wasFiredFromShip):
        self.x = x
        self.y = y
        self.hasHit = False
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
                    self.hasHit = True
            if theBoss.damage(self.x, self.y):
                self.hasHit = True
            if self.y < 0:
                self.isAlive = False
        else:
            if player.wasHit(self.x, self.y):
                self.hasHit = True
            if self.y > SCREEN_H:
                self.isAlive = False
        if self.hasHit:
            self.isAlive = False
