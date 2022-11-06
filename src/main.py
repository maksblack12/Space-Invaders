import pygame
from player import *
from settings import *
from bullet import *
from alien import *
from boss import *
from image_manager import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

imageManager = ImageManager()

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        aliens.clear()

    ### Update all entities
    player.update(keys, bullets)

    for alien in aliens:
        alien.update(bullets)

    for bullet in bullets:
        bullet.update(aliens, theBoss, player)

    aliens = [alien for alien in aliens if alien.isAlive]
    bullets = [bullet for bullet in bullets if bullet.isAlive]

    theBoss.update(aliens, bullets, player)

    if player.hp <= 0 or theBoss.hp <= 0:
        run = False

    ### Draw game
    screen.fill(DARK_BLUE)

    for alien in aliens:
        alien.draw(screen, imageManager)

    for bullet in bullets:
        bullet.draw(screen, theBoss, imageManager)

    theBoss.draw(screen, imageManager)

    player.draw(screen, imageManager)

    boss_font = pygame.font.Font('rsrc/font/scaryBoss.ttf', 32)
    font = pygame.font.Font('rsrc/font/Gloomy_Things.ttf', 20)

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

    font = pygame.font.Font('rsrc/font/Gloomy_Things.ttf', 32)

    text = font.render(player.getHp(), True, [255, 0, 0])
    textRect = text.get_rect()
    textRect.center = (SCREEN_W-40, 10)

    screen.blit(text, textRect)
    pygame.display.update()
