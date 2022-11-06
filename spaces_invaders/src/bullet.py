from settings import *

class PewPew:
    def __init__(self, x, y, wasFiredFromShip):
        self.x = x
        self.y = y
        self.hasHit = False
        self.wasFiredFromShip = wasFiredFromShip

    def move(self):
        if self.wasFiredFromShip:
            self.y-=BULLET_SPEED
        else:
            self.y+=BULLET_SPEED
