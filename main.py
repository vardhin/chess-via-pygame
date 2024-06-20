import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    '''hi 
    bro'''

