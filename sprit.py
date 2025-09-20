import pygame

class Sprit(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface((w, h))   
        self.image.fill(color)                
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)            
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Two Sprites")
obj1 = Sprit(30, 30, 60, 60, (255, 0, 0))   
obj2 = Sprit(200, 200, 100, 50, (0, 0, 255)) 
group = pygame.sprite.Group(obj1, obj2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
         obj1.rect.x -= 1
    if keys[pygame.K_RIGHT]:
        obj1.rect.x += 1
    if keys[pygame.K_UP]:
        obj1.rect.y -= 1
    if keys[pygame.K_DOWN]:
        obj1.rect.y += 1
    screen.fill((0, 0, 0))     
    group.draw(screen)         
    pygame.display.flip()      
