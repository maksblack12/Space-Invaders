import pygame
from random import randint
from TheShip import TheShip
from TheSettings import *
from PewPew import *
from MrAlien import *
from TheBoss import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
alien_img=pygame.image.load("rsrc/alien.png")
alien_img=pygame.transform.scale(alien_img, (100, 100))
boss_img = pygame.image.load("rsrc/boss.png")
boss_img = pygame.transform.scale(boss_img, (300, 300))
ship_img=pygame.image.load("rsrc/space-invaders.png")
ship_img=pygame.transform.scale(ship_img, (100,100))
bullet_img = pygame.image.load("rsrc/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (18, 48))
aliens_bullet_img = pygame.image.load("rsrc/aliens_attack.png")
aliens_bullet_img = pygame.transform.scale(aliens_bullet_img, (18, 48))
boss_bullet_img = pygame.image.load("rsrc/boss_attack.png")
boss_bullet_img = pygame.transform.scale(boss_bullet_img, (32, 32))
with open("src/bossAlive.txt", "w") as file:
    file.write("False")
screen.fill(DARK_BLUE)
clock = pygame.time.Clock()


ship = TheShip(SCREEN_W/2-100/2, SCREEN_H-100)

theBoss=TheBoss()

bullets = []
aliens = []
aliens_attack = []

for x in range(0,SCREEN_W-300,150):
    aliens.append(MrAlien(x+30, 217))
    aliens.append(MrAlien(x, 117))
    aliens.append(MrAlien(x+10, 317))

run=True

while run:
    clock.tick(60)
    ### player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    if ship.Hp <= 0:
        run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move_left()
    if keys[pygame.K_RIGHT]:
        ship.move_right()
    if keys[pygame.K_SPACE] and ship.CouldIShoot():
        bullets.append(PewPew(ship.x+42, SCREEN_H-100, True))
    if keys[pygame.K_l] and ship.Laser():
        for l in range(0, 5):
            bullets.append(PewPew(ship.x+42, SCREEN_H-100, True))
    if keys[pygame.K_s]:
        print("ssss")
    if keys[pygame.K_c]:
        aliens=[]
        # aliens.append(MrAlien(ship.x, 200))

    screen.fill(DARK_BLUE)
    # The fors first check if the bad guy got hit then draw the hole thing (very important!)
    for alien in aliens:
        for bullet in bullets:
            if alien.hit(bullet.x, bullet.y):
                bullet.hitTheTarget=True
        screen.blit(alien_img, alien.coords())
    screen.blit(ship_img, ship.TheCoords())

    for attack in aliens_attack:
        if ship.hit(attack.x, attack.y):
            attack.hitTheTarget=True


    for alien in aliens:
        if alien.x<=0:
            MrAlien.runGuysRun=ALIEN_SPEED
        if alien.x >=SCREEN_W-100:
            MrAlien.runGuysRun =- ALIEN_SPEED

    for alien in aliens:
        alien.runRunRun()
        if alien.CanIPlsShoot():
            aliens_attack.append(PewPew(alien.x+45, alien.y+55, False))

    for bullet in bullets:
        screen.blit(bullet_img, (bullet.x, bullet.y))
        bullet.move()
    for attack in aliens_attack:
        if theBoss.bossAlive==False:
            screen.blit(aliens_bullet_img, (attack.x, attack.y))
        else:
            screen.blit(boss_bullet_img, (attack.x, attack.y))
        attack.move()

    boss_font = pygame.font.Font('rsrc/scaryBoss.ttf', 32)
    font = pygame.font.Font('rsrc/Gloomy_Things.ttf', 20)

    boss_health = boss_font.render(theBoss.myDeathTimer(), True, [255, 0, 0])
    boss_bar = boss_font.render("__________", True, [255, 0, 0])
    inform = font.render("The boss has slowd down your bullets", True, [0, 255, 0])

    bossRect = boss_health.get_rect()
    bossBarRect = boss_bar.get_rect()
    inform_rect = inform.get_rect()

    bossRect.center = (SCREEN_W/2, 15)
    bossBarRect.center = (SCREEN_W/2, 40)
    inform_rect = (SCREEN_W/2-150, 60)

    if not aliens:
        with open("src/bossAlive.txt", "w") as file1:
            file1.write("True")
        theBoss.bossAlive=True


    if theBoss.bossHp>0 and theBoss.bossAlive:
        screen.blit(boss_health, bossRect)
        screen.blit(boss_bar, bossBarRect)
        screen.blit(inform, inform_rect)
        screen.blit(boss_img, (450, 217))
        ship.bullet_delay=700


    for bullet in bullets:
        if theBoss.ouch(bullet.x, bullet.y):
            bullet.hitTheTarget = True

    if theBoss.bossHp==25:
            aliens_attack.append(PewPew(SCREEN_W/2+400, 0, False))

    if theBoss.bossHp==15 and theBoss.spawnMinion==False:
        aliens.append(MrAlien(200, 217))
        aliens.append(MrAlien(SCREEN_W/2, 217))
        aliens.append(MrAlien(SCREEN_W-500, 217))
        aliens.append(MrAlien(SCREEN_W-300, 217))
        aliens.append(MrAlien(500, 217))
        theBoss.spawnMinion=True

    if theBoss.bossHp==10 and theBoss.regen==False:
        for i in range(0,19):
            aliens_attack.append(PewPew(theBoss.x+150, theBoss.y+150, False))
        theBoss.bossHp+=5
        theBoss.regen=True

    if theBoss.bossHp<=0:
        run = False

    font = pygame.font.Font('rsrc/Gloomy_Things.ttf', 32)

    text = font.render(ship.myHealthStatus(), True, [255, 0, 0])

    textRect = text.get_rect()

    textRect.center = (SCREEN_W-40, 10)

    screen.blit(text, textRect)

    bullets=[bullet for bullet in bullets if bullet.y>=0 and not bullet.hitTheTarget]
    aliens_attack=[attack for attack in aliens_attack if attack.y<=SCREEN_H and not attack.hitTheTarget]
    aliens=[alien for alien in aliens if alien.isAlive]
    pygame.display.update()
