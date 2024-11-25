# переміщування квадратика
import pygame
import random
import sys

# ініціалізація pygame
pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch the Square')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
score = 0
square_size = 50
x = random.randint(0, WIDTH - square_size)
y = random.randint(0, HEIGHT - square_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # координати - (10, 20)
            if x <= mouse_pos[0] <= x + square_size and y <= mouse_pos[1] <= y + square_size:
                score += 1
                x = random.randint(0, WIDTH - square_size)
                y = random.randint(0, HEIGHT - square_size)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))

    # відображення рахунку
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, BLUE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)


pygame.quit()
sys.exit()

