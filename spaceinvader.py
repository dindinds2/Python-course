import math
import random
import pygame

screen_width = 900
screen_height = 900
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 5
enemy_speed_y = 30
bullet_speed_y = 40
collision_distance = 27
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('background2.jpg')
pygame.display.set_caption("Space Invader Game")
icon = pygame.image.load('ufo.jpg')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('player1.jpg')
playerX = player_start_x
playerY = player_start_y
playerX_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.jpg'))
    enemyX.append(random.randint(0,screen_width-64))
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = player_start_y
bulletX_change = 0
bulletY_change = bullet_speed_y
bullet_state = "Ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf',64)
music_file = "background2.ogg"
pygame.mixer.music.load(music_file)
def show_score(x,y):
    score = font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg,(x+16,y+10))
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((enemyX - bulletX)**2+(enemyY-bulletY)**2)
    return distance < collision_distance
running = True
while running:
    screen.fill((0,0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "Ready":
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP and event.key  in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change = 0
    playerX += playerX_change
    playerX = max(0,min(playerX,screen_width-64))
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= screen_width - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        if iscollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY = player_start_y
            bullet_state = "Ready"
            score_value += 1
            enemyX[i] = random.randint(0,screen_width-64)
            enemyY[i] = random.randint(enemy_start_y_min,enemy_start_y_max)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY <= 0 :
        bulletY = player_start_y
        bullet_state = "Ready"
    elif bullet_state == "Fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()