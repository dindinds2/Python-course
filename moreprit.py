import pygame

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Program')
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
player = Rect(100,200,100,100,(0, 0, 255))
enemy1 = Rect(200,200,100,100,(255, 0, 0))
enemy2 = Rect(300,300,100,100,(0, 255, 0))
enemy3 = Rect(400,400,100,100,(0, 0, 255))
enemy4 = Rect(500,500,100,100,(255, 0, 0))
enemy5 = Rect(600,600,100,100,(255, 0, 0))
group = pygame.sprite.Group(player,enemy1,enemy2,enemy3,enemy4,enemy5)
score_value = 0
over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
player_speed_x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        group.draw(screen)
        show_score(textX,textY)
        pygame.display.update()
        pygame.display.flip()
pygame.quit()