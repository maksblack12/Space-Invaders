import pygame
from player import *
from settings import *
from bullet import *
from alien import *
from boss import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
alien_img=pygame.image.load("rsrc/alien.png")
alien_img = pygame.transform.scale(alien_img, ALIEN_SIZE)
boss_img = pygame.image.load("rsrc/boss.png")
boss_img = pygame.transform.scale(boss_img, (300, 300))
player_img=pygame.image.load("rsrc/player.png")
player_img = pygame.transform.scale(player_img, (100, 100))
player_shield_img=pygame.image.load("rsrc/player_shield.png")
player_shield_img = pygame.transform.scale(player_shield_img, (100, 100))
bullet_img = pygame.image.load("rsrc/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (18, 48))
aliens_bullet_img = pygame.image.load("rsrc/aliens_attack.png")
aliens_bullet_img = pygame.transform.scale(aliens_bullet_img, (18, 48))
boss_bullet_img = pygame.image.load("rsrc/boss_attack.png")
boss_bullet_img = pygame.transform.scale(boss_bullet_img, (100, 100))
screen.fill(DARK_BLUE)
clock = pygame.time.Clock()

theBoss = Boss(SCREEN_W/2,SCREEN_H/2)

player = Player(SCREEN_W/2-100/2, SCREEN_H-100, theBoss)


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
    if player.hp <= 0:
        run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.moveLeft()
    if keys[pygame.K_d]:
        player.moveRight()
    if keys[pygame.K_SPACE] and player.isShotPossible():
        bullets.append(Bullet(player.x+42, SCREEN_H-100, True))
    if keys[pygame.K_w] and player.isLaserPossible():
        for i in range(0, 5):
            bullets.append(Bullet(player.x+42, SCREEN_H-100-50*i, True))
    if keys[pygame.K_c]:
        aliens.clear()

    player.updateShield(keys[pygame.K_s])

    screen.fill(DARK_BLUE)
    # The loops first check if the bad guy got hit then draw the hole thing (very important!)
    for alien in aliens:
        for bullet in bullets:
            if alien.hit(bullet.x, bullet.y):
                bullet.hasHit=True
        screen.blit(alien_img, alien.position())
    screen.blit(player_img, player.position())
    if (player.hasShield):
        screen.blit(player_shield_img, player.position())

    for attack in aliens_attack:
        if player.wasHit(attack.x, attack.y):
            attack.hasHit=True


    for alien in aliens:
        if alien.x<=0:
            MrAlien.globalSpeed=ALIEN_SPEED
        if alien.x >=SCREEN_W-100:
            MrAlien.globalSpeed =- ALIEN_SPEED

    for alien in aliens:
        alien.updatePosition()
        if alien.isShotPossible():
            aliens_attack.append(Bullet(alien.x+45, alien.y+55, False))

    for bullet in bullets:
        screen.blit(bullet_img, (bullet.x, bullet.y))
        bullet.move()
    for attack in aliens_attack:
        if theBoss.isAlive==False:
            screen.blit(aliens_bullet_img, (attack.x, attack.y))
        else:
            screen.blit(boss_bullet_img, (attack.x, attack.y))
        attack.move()

    boss_font = pygame.font.Font('rsrc/scaryBoss.ttf', 32)
    font = pygame.font.Font('rsrc/Gloomy_Things.ttf', 20)

    boss_health = boss_font.render(theBoss.getHp(), True, [190, 0, 0])
    boss_bar = boss_font.render("__________", True, [190, 0, 0])
    inform = font.render("The boss has slowd down your bullets!", True, [255, 0, 0])
    inform2 = font.render("The boss has upgraded the aliens!", True, [255, 0, 0])

    bossRect = boss_health.get_rect()
    bossBarRect = boss_bar.get_rect()
    inform_rect = inform.get_rect()
    inform_rect2 = inform2.get_rect()

    bossRect.center = (SCREEN_W/2, 15)
    bossBarRect.center = (SCREEN_W/2, 40)
    inform_rect = (SCREEN_W/2-150, 60)
    inform_rect2 = (SCREEN_W/2-135, 80)

    if not aliens:
        theBoss.isAlive=True


    if theBoss.hp>0 and theBoss.isAlive:
        screen.blit(boss_health, bossRect)
        screen.blit(boss_bar, bossBarRect)
        screen.blit(inform, inform_rect)
        screen.blit(inform2, inform_rect2)
        screen.blit(boss_img, (450, 217))
        player.bulletDelay=700


    for bullet in bullets:
        if theBoss.damage(bullet.x, bullet.y):
            bullet.hasHit = True

    if theBoss.hp==25:
            aliens_attack.append(Bullet(SCREEN_W/2+400, 0, False))

    if theBoss.hp==15 and theBoss.spawnMinion==False:
        aliens.append(MrAlien(200, 217))
        aliens.append(MrAlien(SCREEN_W/2, 217))
        aliens.append(MrAlien(SCREEN_W-500, 217))
        aliens.append(MrAlien(SCREEN_W-300, 217))
        aliens.append(MrAlien(500, 217))
        theBoss.spawnMinion=True

    if theBoss.hp==10 and theBoss.regenerateHp==False:
        for i in range(0,19):
            aliens_attack.append(Bullet(theBoss.x+145, theBoss.y+150, False))
        theBoss.hp+=5
        theBoss.regenerateHp=True

    if theBoss.hp<=0:
        run = False

    font = pygame.font.Font('rsrc/Gloomy_Things.ttf', 32)

    text = font.render(player.getHp(), True, [255, 0, 0])

    textRect = text.get_rect()

    textRect.center = (SCREEN_W-40, 10)

    screen.blit(text, textRect)

    bullets=[bullet for bullet in bullets if bullet.y>=0 and not bullet.hasHit]
    aliens_attack=[attack for attack in aliens_attack if attack.y<=SCREEN_H and not attack.hasHit]
    aliens=[alien for alien in aliens if alien.isAlive]
    pygame.display.update()
