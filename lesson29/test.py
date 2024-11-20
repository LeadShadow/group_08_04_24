from pathlib import Path

import pygame
import time

# pygame.display

pygame.init()

screen = pygame.display.set_mode(size=(1400.00, 800.00))

pygame.display.get_surface()
pygame.display.update()
pygame.display.flip()

# pygame.draw
WHITE = (255, 255, 255)  # RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
pygame.draw.line(screen, RED, (100, 100), (700, 500), width=5)
pygame.display.flip()
pygame.draw.rect(screen, GREEN, rect=pygame.Rect(100, 100, 100, 100), width=5)
pygame.display.flip()

# pygame.image
pygame.image.load(Path('depositphotos_10888323-stock-photo-british-shorthair-cat-7-months.jpg'))
pygame.display.flip()
time.sleep(5)
pygame.image.save(screen, Path('depositphotos_10888323-stock-photo-british-shorthair-cat-7-months.jpg'))
pygame.display.flip()
time.sleep(5)

# pygame.mixer
# sound = pygame.mixer.Sound('')
# sound.play()
# sound.stop()
#
# pygame.mixer.music.load('')
# pygame.mixer.music.play(loops=1)
# pygame.mixer.music.stop()

# pygame.font - рендеринг тексту

# font = pygame.font.Font('')
font = pygame.font.SysFont('Times New Roman', 36)
text_surface = font.render('Hello world!', True, GREEN)
screen.blit(text_surface, (100, 100))
pygame.display.flip()
time.sleep(5)