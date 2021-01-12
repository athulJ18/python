import pygame as pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

# initializing
pygame.init()
window = pygame.display.set_mode((1200, 720))
pygame.display.set_caption('Dodge the missile')


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
            running = False
    
    
