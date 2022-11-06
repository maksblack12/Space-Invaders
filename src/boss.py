from settings import *
from alien import *
from bullet import *

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

    def update(self, aliens, bullets, player):
        if not aliens:
            self.isAlive = True
        if self.hp > 0 and self.isAlive:
            player.bulletDelay = 700
        if self.hp == 25:
            bullets.append(Bullet(SCREEN_W/2+400, 0, False))
        if self.hp == 15 and self.spawnMinion == False:
            aliens.append(MrAlien(200, 217))
            aliens.append(MrAlien(SCREEN_W/2, 217))
            aliens.append(MrAlien(SCREEN_W-500, 217))
            aliens.append(MrAlien(SCREEN_W-300, 217))
            aliens.append(MrAlien(500, 217))
            self.spawnMinion = True
        if self.hp == 10 and self.regenerateHp == False:
            for i in range(0, 19):
                bullets.append(Bullet(self.x+145, self.y+150, False))
            self.hp += 5
            self.regenerateHp = True

    def getHp(self):
        return f"{self.hp}|{self.maxHp}"

    def draw(self, screen, imageManager):
        if self.hp > 0 and self.isAlive:
            screen.blit(imageManager.get("boss"), (450, 217))

