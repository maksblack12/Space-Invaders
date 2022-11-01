from TheSettings import *

class TheBoss:
    def __init__(self):
        self.x = 450
        self.y = 217
        self.bossMaxHp=30
        self.bossHp=self.bossMaxHp
        self.bossAlive=False
        self.spawnMinion=False
        self.laserLeft=False
        self.regen=False

    def ouch(self, bullet_x, bullet_y):
        if self.bossAlive and self.x < bullet_x < self.x+200 and self.y < bullet_y < self.y+100:
            self.bossHp -= 1
            return True
        return False

    def myDeathTimer(self):
        return f"{self.bossHp}|{self.bossMaxHp}"
