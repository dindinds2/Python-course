import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
title = pygame.display.set_caption('my_first_screen.exe')
red = (225,0,0)
x,y = 290,250

text = pygame.font.Font(None,58).render('Hello there',True,pygame.Color('red'))
tect_rect = text.get_rect(center =(640 //2 , 480//2 +110))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    screen.fill((255,255,255))
    pygame.draw.rect(screen,red,pygame.Rect(x,y,60,60))
    screen.blit(text,tect_rect)
    pygame.display.flip()
pygame.quit()

