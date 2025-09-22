import pygame

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Program')
obj = Rect(60, 60, 30, 50, (255, 255, 255))
obj2 = Rect(120, 120, 60, 60, (255, 255, 255))
group = pygame.sprite.Group(obj, obj2)
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)
colors = [(255,0,0), (0,255,0), (0,0,255)]
index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR:
            index = (index + 1) % len(colors)
            obj.image.fill(colors[index])
            obj2.image.fill(colors[(index+1) % len(colors)])
    screen.fill((255,255,255))
    group.draw(screen)
    pygame.display.flip()

pygame.quit()
