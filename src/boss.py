from settings import *

class Boss:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.maxHp=30
        self.hp=self.maxHp
        self.isAlive=False
        self.spawnMinion=False
        self.regenerateHp=False

    def damage(self, bullet_x, bullet_y):
        if self.isAlive and self.x+EYE_SIZE[0] < bullet_x < self.x+EYE_SIZE[2] and self.y+EYE_SIZE[1] < bullet_y < self.y+EYE_SIZE[3]:
            self.hp -= 1
            return True
        return False

    def getHp(self):
        return f"{self.hp}|{self.maxHp}"

