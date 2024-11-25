# переміщування квадратика
import pygame
import sys

# ініціалізація pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move the Square')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
x, y = 100, 100
speed = 5
square_size = 70

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обробка натискання клавіш
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
