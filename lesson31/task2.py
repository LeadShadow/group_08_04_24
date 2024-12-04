# Переслідування кульки
# Квадрат керується гравцем, а кулька намагається "втекти". Якщо гравець
# торкнеться кульки, гра завершується.
import random

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chase tha ball')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

square = pygame.Rect(100, 100, 50, 50)
ball = pygame.Rect(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 30, 30)

ball_speed = [7, 7]
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.y -= speed
    if keys[pygame.K_DOWN]:
        square.y += speed
    if keys[pygame.K_LEFT]:
        square.x -= speed
    if keys[pygame.K_RIGHT]:
        square.x += speed

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = - ball_speed[0]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = - ball_speed[1]

    if square.colliderect(ball):
        print('Фігури зіткнулись!')
        running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, square)
    pygame.draw.ellipse(screen, BLUE, ball)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
