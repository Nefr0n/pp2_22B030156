import pygame
from pygame.locals import *
import random
pygame.init()
height = 800
width = 500

speed = 2
score = 0
gameover = False

leftLane = 150
midLane = 250
rigthLane = 350
lanes = [leftLane, midLane, rigthLane]

laneMoveY = 0

colors = {
    'green': (125, 180, 80)
    }

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car racing")

running = True

clock = pygame.time.Clock()
fps = 120

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        imageScale = 100 / image.get_rect().width
        newWidth = image.get_rect().width * imageScale
        newHeight = image.get_rect().height * imageScale
        self.image = pygame.transform.scale(image, (newWidth, newHeight))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class PlayersVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load("images/car.png")
        super().__init__(image, x, y)

playerX = 250
playerY = 600

player_group = pygame.sprite.Group()

player = PlayersVehicle(playerX, playerY)
player_group.add(player)

vehicle_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()


class Money(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        imageScale = 50 / image.get_rect().width
        newWidth = image.get_rect().width * imageScale
        newHeight = image.get_rect().height * imageScale
        self.image = pygame.transform.scale(image, (newWidth, newHeight))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.center[0] < rigthLane:
                player.rect.x += 100
            if event.key == pygame.K_LEFT and player.rect.center[0] > leftLane:
                player.rect.x -= 100

            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True

                    if event.key == pygame.K_LEFT:
                        player.rect.left = vehicle.rect.right
                    elif event.key == pygame.K_RIGHT:
                        player.rect.right = vehicle.rect.left

            for money in money_group:
                if pygame.sprite.collide_rect(player, money):
                    score += 3
                if pygame.sprite.collide_rect(vehicle, money):
                    money.kill()
            
                


    

    win.fill((130,125,100))
   
    

    #draw marks
    pygame.draw.rect(win, colors['green'], (100, 0, 300, height))#whole lane
    pygame.draw.rect(win, (255, 232, 0), (95, 0, 15, height)) #left lane's mark
    pygame.draw.rect(win, (255, 232, 0), (395, 0, 15, height))#right lane's mark

    laneMoveY += speed * 2
    if laneMoveY >= 50 * 2:
        laneMoveY = 0

    for y in range(-2 * 50, height, 50 * 2):
        pygame.draw.rect(win, (255,255,255), (45 + leftLane, y + laneMoveY, 15, 50))
        pygame.draw.rect(win, (255,255,255), (45 + midLane, y + laneMoveY, 15, 50))
    
    player_group.draw(win)
    addVehicle = True
    addmoney = True

    for vehicle in vehicle_group:
        if vehicle.rect.top < vehicle.rect.height * 1.5:
            addVehicle = False

    for money in money_group:
        if money.rect.top < vehicle.rect.height * 1.5:
            addmoney = False

    
    if addVehicle:
        lane = random.choice(lanes)

        image = pygame.image.load("images/carvec.png")

        vehicle = Vehicle(image, lane, height/-2)
        vehicle_group.add(vehicle)
    
    for vehicle in vehicle_group:
        vehicle.rect.y += speed


        if vehicle.rect.top >= height:
            vehicle.kill()

            score += 1

            if score > 0 and score % 5 == 0:
                speed +=1 
    

    if addmoney:
        
        lane = random.choice(lanes)

        image = pygame.image.load("images/money.png")
        money = Money(image, lane, height/-2)
        money_group.add(money)
    
    for money in money_group:
        if speed < 5:
            money.rect.y += speed
        else :
            money.rect.y += speed - 2

        if money.rect.top >= height:
            money.kill()



    money_group.draw(win)
    vehicle_group.draw(win)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score ' + str(score), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (50, 400)
    win.blit(text, textRect)

    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
    
    if pygame.sprite.spritecollide(player, money_group, True):
        score += 2
    if pygame.sprite.spritecollide(vehicle, money_group, True):
        money.kill()

    if gameover:
        pygame.draw.rect(win, (255,0,0), (0,50,width,100))

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Yes or No)', True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (width/2, 100)
        win.blit(text, textRect)

    pygame.display.update()
    
    while gameover:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [playerX, playerY]
                elif event.key == pygame.K_n:
                    gameover = False
                    running = False

    
    clock.tick(fps)
pygame.quit()