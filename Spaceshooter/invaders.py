import sys

import pygame

import random

import math

pygame.init()
pygame.display.set_caption('space invaders')
screen = pygame.display.set_mode((500,600))
clock = pygame.time.Clock()
x ,y = 240,500


pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 30)

#ship
ship = pygame.image.load('spaceship.png')    
ship.set_colorkey((0,0,0)) 
scaled = pygame.transform.scale(ship,(30,30))


player_change = 0

def player_movement(x,y):
    screen.blit(scaled,(x,y))

num = 6
monster = []
monster_x = []
monster_y = []
mon_change = []

for i in range(num):
    monster.append(pygame.image.load('monster.png').convert_alpha())
    monster[i].set_colorkey((0,0,0))
    monster_x.append(random.randint(1,450))
    monster_y.append(random.randint(1,150))
    mon_change.append(3)

#bullet
bullet = pygame.image.load('bullet.png')

bullet_change = 7
bullet_state = 'ready'
bullet_y = y
bullet_x = 0


def bullet_movement(bullet_x , bullet_y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet,(bullet_x,bullet_y))

def isCollison(monster_x , monster_y , bullet_x , bullet_y):
    distance =  math.sqrt((math.pow(monster_x - bullet_x,2))+ (math.pow(monster_y - bullet_y,2)))
    if distance < 24 :
        return True
    else:
        return False
    
score = 0

def playCollison(x, y ,monster_x ,monster_y):
   playerdistance =  math.sqrt((math.pow(x - monster_x,2))+ (math.pow(y - monster_y,2)))
   if playerdistance < 32:
       return True
   else:
       return False

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -3

            if event.key == pygame.K_RIGHT:
                player_change = 3

            if event.key == pygame.K_SPACE:
               
                if bullet_state == 'ready':
                     bullet_x = x
                     bullet_movement(bullet_x , bullet_y)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

            

    x+= player_change
   

    if x <= 0:
        x = 0

    if x>= 500-30:
        x = 500 -30
    for i in range(num):
        monster_x[i]+= mon_change[i]

        if monster_x[i] <= 0:
            monster_x[i] = 0
            monster_y[i]+= 20
            mon_change[i]*= -1

        if monster_x[i]>= 500-32:
            monster_x[i]= 500-32
            monster_y[i]+= 20
            mon_change[i]*= -1


        playerCollison = playCollison(x, y ,monster_x[i], monster_y[i])
        if playerCollison == True:
            text = my_font.render('GAME OVER',True, (255,255,255))
            screen.blit(text, (150,200))
            run = False

        collison = isCollison(monster_x[i] , monster_y[i] , bullet_x , bullet_y)
        if collison == True:
            bullet_y = 500
            bullet_state = 'ready'
            monster_x[i] = random.randint(1,450)
            monster_y[i] = random.randint(1,150)
            score+=1
            
        text_surface = my_font.render(str(score), True, (255, 255, 255))
           
           
        screen.blit(text_surface,(250,250))

        screen.blit(monster[i],(monster_x[i],monster_y[i]))

        
    
    if bullet_state == 'fire':
        bullet_movement(bullet_x,bullet_y)
        bullet_y-=bullet_change

        if bullet_y <=0:
            bullet_y = y
            bullet_state = 'ready'

 


        

    pygame.display.update()
    screen.fill((0,0,0))
    player_movement(x,y)
    
    
    clock.tick(60)


            


