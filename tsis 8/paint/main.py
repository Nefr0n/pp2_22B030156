import pygame


pygame.init()


FPS = 60
WIDTH, HEIGHT = 500, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Buttom Demo')

brush = pygame.image.load('assets/brush_button.jpeg').convert_alpha()
erase = pygame.image.load('assets/erase_button.jpg').convert_alpha()

class Buttons():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
