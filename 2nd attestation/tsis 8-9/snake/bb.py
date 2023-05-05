import pygame, sys
from pygame.locals import *
width, height = 600, 800
pygame.init()
pygame.display.set_caption("Phone Book")
surf = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class obj:
    def update(self, curr_point):
        return
    
class RectButton(obj):
    def __init__(self):
        # attributes of rectangle button
        self.width = 50
        self.rect = pygame.Rect(width // 2 - self.width, 20, self.width, self.width)
        self.isButton = True    
rect = Rect(135, 190, 330, 80)
rect1 = Rect(135, 350, 330, 80)
rect2= Rect(135, 510, 330, 80)

#textish Title
font = pygame.font.SysFont('gabriola', 90)
img = font.render("PHONE BOOK", True, (10, 10, 10))

#textish 1st button
font = pygame.font.SysFont('gabriola', 90)
img = font.render("PHONE BOOK", True, (10, 10, 10))
#textish 2nd button
font = pygame.font.SysFont('gabriola', 65)
img1 = font.render("Contacks", True, (10, 10, 10))
#textish 3rd button
font = pygame.font.SysFont('gabriola', 65)
img2 = font.render("Add contacts", True, (10, 10, 10))
#textish 4th button
font = pygame.font.SysFont('gabriola', 65)
img3 = font.render("Read files", True, (10, 10, 10))


while True:

        surf.fill((110, 231, 222))

        surf.blit(img, (85, 65))
        
        # running for every user input
        for event in pygame.event.get():
            # quit event type
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.draw.rect(surf, (210, 56, 66), rect, 0, 18)
        pygame.draw.rect(surf, (210, 56, 66), rect1, 0, 18)
        pygame.draw.rect(surf, (210, 56, 66), rect2, 0 ,18)
        surf.blit(img1, (206, 200))
        surf.blit(img2, (176, 363))
        surf.blit(img3, (207, 520))
        pygame.display.update()
