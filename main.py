import pygame
pygame.init()

GREY = (60,60,60)
CEMENT = (190,190,190)
HEIGHT = 1000
WIDTH = 1300
SQUARE_SIZE = 110
ROWS = 8
COLS = 8
x_of_grids = 60
y_of_grids = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Initial Window Title')


class Square:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x_of_grids, y_of_grids, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

squares = []
for row in range(ROWS):
    row_squares = []
    for col in range(COLS):
        x_of_grids = 200 + col * SQUARE_SIZE
        y_of_grids = 60 + row * SQUARE_SIZE
        color = CEMENT if (row + col) % 2 == 0 else GREY
        square = Square(x_of_grids, y_of_grids, SQUARE_SIZE, color)
        row_squares.append(square)
    squares.append(row_squares)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
            elif event.key == pygame.K_UP:
                print("Up arrow key pressed")
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed")

    screen.fill((100,150,150))

    for row in squares:
        for square in row:
            square.draw(screen)

    pygame.display.update()
    
