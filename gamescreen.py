import pygame

pygame.init()
scree = pygame.display.set_mode((300,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()