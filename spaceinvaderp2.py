import pygame
import random
import time

pygame.init()

pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('enemy Dodger')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background1.png')

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 420
playerX_change = 0
player_speed = 5

enemyImg = pygame.image.load('enemy.png')
enemy_width = 64
enemy_height = 64

num_of_enemies = 5
enemies = []

for _ in range(num_of_enemies):
    x = random.randint(0, SCREEN_WIDTH - enemy_width)
    y = random.randint(-150, -150)
    speed = random.randint(3, 6)
    enemies.append([x, y, player_speed])

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

score_value = 0
start_time = time.time()
font = pygame.font.Font('freesansbold.ttf', 32)

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score = int((score_value))
    text = font.render(f'time survived: {score} s', True, WHITE)
    screen.blit(text, (10, 10))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def is_collision(enemyX, enemyY, playerX, playerY):
    distance = ((enemyX - playerX) ** 2 + (enemyY - playerY) ** 2) ** 0.5
    return distance < 40

def game_over_text():
    over_text = over_font.render('game over', True, WHITE)
    screen.blit(over_text, (200, 220))

running = True
game_over = False

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
            elif event.key == pygame.K_RIGHT:
                playerX_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0``

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

        # Move and draw enemies
        for i in range(num_of_enemies):
            enemies[i][1] += enemies[i][2]

            # Respawn enemy at the top
            if enemies[i][1] > SCREEN_HEIGHT:
                enemies[i][0] = random.randint(0, SCREEN_WIDTH - enemy_width)
                enemies[i][1] = random.randint(-150, -50)
                enemies[i][2] = random.randint(3, 6)

            # Collision detection
            if is_collision(enemies[i][0], enemies[i][1], playerX, playerY):
                game_over = True

            enemy(enemies[i][0], enemies[i][1])

        # Update score
        score_value = time.time() - start_time

    player(playerX, playerY)

    if game_over:
        game_over_text()
    else:
        show_score()

    pygame.display.update()