import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
GREEN = (0,255,0)
pygame.draw.circle(screen,GREEN,(300,300),50)
pygame.draw.circle(screen,GREEN,(100,100),50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()