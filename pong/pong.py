# Instagram --> glegital

import pygame
pygame.init()

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 550

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


player1_x = 0
player1_y = 245
player1_speed = 0 

player2_x = 635
player2_y = 245
player2_speed = 0

ball_x =  325
ball_y = 275
ball_x_speed = 3
ball_y_speed = 3 

scoreBlue = 0
scoreRed = 0

speed = 60

font = pygame.font.Font(None, 30)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
bg = pygame.image.load('assets/bg.png')
ball_img = pygame.image.load('assets/ball.jpeg')
player1_img = pygame.image.load('assets/player1.jpeg')
player2_img = pygame.image.load('assets/player2.jpeg')

run = True

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_w:
                player1_speed = -3
            if event.key == pygame.K_s:
                player1_speed = 3
            
            #Player 2
            if event.key == pygame.K_UP:
                player2_speed = -3
            if event.key == pygame.K_DOWN:
                player2_speed = 3

        if event.type == pygame.KEYUP:
            #Player 1
            if event.key == pygame.K_w:
                player1_speed = 0
            if event.key == pygame.K_s:
                player1_speed = 0
            
            #Player 2
            if event.key == pygame.K_UP:
                player2_speed = 0
            if event.key == pygame.K_DOWN:
                player2_speed = 0
                
    if ball_y > 540 or ball_y < 10:

        ball_y_speed *= -1
    
    if ball_x > 650 :

        ball_x = 325
        ball_y = 275
        ball_x_speed *= -1
        ball_y_speed *= -1
        speed = 60
        scoreBlue += 1

    if  ball_x < 0:

        ball_x = 325
        ball_y = 275
        ball_x_speed *= -1
        ball_y_speed *= -1
        speed = 60
        scoreRed += 1


    player1_y += player1_speed
    player2_y += player2_speed
    
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    screen.blit(bg, (0, 0))

    player1 = screen.blit(player1_img, (player1_x, player1_y))
    player2 = screen.blit(player2_img, (player2_x, player2_y))
    ball = screen.blit(ball_img, (ball_x, ball_y))
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_x_speed *= -1
        speed += 5
    blueMarker = font.render(str(scoreBlue),0,(51,97,255))
    redMarker = font.render(str(scoreRed),0,(200,60,80))

    screen.blit(blueMarker, (526,20))
    screen.blit(redMarker, (88,20))

    pygame.display.flip()
        
    clock.tick(speed)




pygame.quit()
