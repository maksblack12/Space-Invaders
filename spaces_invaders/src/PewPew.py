class PewPew:
    def __init__(self, x, y, shipAttack):
        self.x = x
        self.y = y
        self.speed = 10
        self.hitTheTarget = False
        self.shipAttack = shipAttack
    def move(self):
        if self.shipAttack:
            self.y-=self.speed
        else:
            self.y+=self.speed
