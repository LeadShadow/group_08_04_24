# переміщування квадратика
import pygame
import sys

# ініціалізація pygame
pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bounce the Ball')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Платформа
platform = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 10)
platform_speed = 7
# кулька
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed = [3, -3]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform.left > 0:
        platform.x -= platform_speed
    if keys[pygame.K_RIGHT] and platform.right < WIDTH:
        platform.x += platform_speed

    # Рух кульки
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= WIDTH:
        # якшо кулька торкається лівої або правої межі екрану
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        # якшо кулька торкається потолка
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(platform):
        ball_speed[1] = -ball_speed[1]

    if ball.bottom >= HEIGHT:
        # якшо кулька торкається нижньої межі екрану
        print('Game over!')
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, platform)
    pygame.draw.ellipse(screen, RED, ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

