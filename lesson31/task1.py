# Керування двома квадратами
# Гравець керує двома квадратами одночасно: один рухається за стрілками, а
# інший — за клавішами WASD. Завдання — уникати зіткнення квадратів.

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Two Squares Control')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

square1 = pygame.Rect(100, 100, 50, 50)
square2 = pygame.Rect(400, 300, 50, 50)

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square1.y -= speed
    if keys[pygame.K_DOWN]:
        square1.y += speed
    if keys[pygame.K_LEFT]:
        square1.x -= speed
    if keys[pygame.K_RIGHT]:
        square1.x += speed

    if keys[pygame.K_w]:
        square2.y -= speed
    if keys[pygame.K_s]:
        square2.y += speed
    if keys[pygame.K_a]:
        square2.x -= speed
    if keys[pygame.K_d]:
        square2.x += speed

    if square1.colliderect(square2):
        print('Квадрати зіткнулись!')
        running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, square1)
    pygame.draw.rect(screen, BLUE, square2)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()
