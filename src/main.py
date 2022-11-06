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

    ### Update all entities
    player.updateShield(keys[pygame.K_s])

    for alien in aliens:
        alien.update(bullets)

    for bullet in bullets:
        bullet.update(aliens, theBoss, player)

    aliens = [alien for alien in aliens if alien.isAlive]
    bullets = [bullet for bullet in bullets if bullet.isAlive]

    theBoss.update(aliens, bullets, player)
    if theBoss.hp <= 0:
        run = False

    ### Draw game
    screen.fill(DARK_BLUE)

    for alien in aliens:
        alien.draw(screen, alien_img)

    for bullet in bullets:
        bullet.draw(screen, bullet_img, theBoss, aliens_bullet_img, boss_bullet_img)

    theBoss.draw(screen, boss_img)

    player.draw(screen, player_img, player_shield_img)

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

    if theBoss.hp>0 and theBoss.isAlive:
        screen.blit(boss_health, bossRect)
        screen.blit(boss_bar, bossBarRect)
        screen.blit(inform, inform_rect)
        screen.blit(inform2, inform_rect2)

    font = pygame.font.Font('rsrc/Gloomy_Things.ttf', 32)

    text = font.render(player.getHp(), True, [255, 0, 0])
    textRect = text.get_rect()
    textRect.center = (SCREEN_W-40, 10)

    screen.blit(text, textRect)
    pygame.display.update()
