import pygame

pygame.init()

# Colors and constants
GREY = (60, 60, 60)
CEMENT = (190, 190, 190)
HEIGHT = 1000
WIDTH = 1300
SQUARE_SIZE = 110
ROWS = 8
COLS = 8
x_of_grids = 60
y_of_grids = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Initial Window Title')

# Define the 3D array for the chessboard
chessboard = [
    [[2], [3], [4], [5], [6], [4], [3], [2]],  # Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
    [[1], [1], [1], [1], [1], [1], [1], [1]],  # Pawns
    [[0], [0], [0], [0], [0], [0], [0], [0]],  # Empty
    [[0], [0], [0], [0], [0], [0], [0], [0]],  # Empty
    [[0], [0], [0], [0], [0], [0], [0], [0]],  # Empty
    [[0], [0], [0], [0], [0], [0], [0], [0]],  # Empty
    [[7], [7], [7], [7], [7], [7], [7], [7]],  # White Pawns
    [[8], [9], [10], [12], [11], [10], [9], [8]],  # Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook
]

# Load images
piece_images = {
    1: 'chess-pack/chess-pawn-black.png',
    2: 'chess-pack/chess-rook-black.png',
    3: 'chess-pack/chess-knight-black.png',
    4: 'chess-pack/chess-bishop-black.png',
    5: 'chess-pack/chess-queen-black.png',
    6: 'chess-pack/chess-king-black.png',
    7: 'chess-pack/chess-pawn-white.png',
    8: 'chess-pack/chess-rook-white.png',
    9: 'chess-pack/chess-knight-white.png',
    10: 'chess-pack/chess-bishop-white.png',
    11: 'chess-pack/chess-queen-white.png',
    12: 'chess-pack/chess-king-white.png'
}

# Create a sprite group
chess_piece_group = pygame.sprite.Group()

# Define the sprite class
class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, piece_type, image_path, position, tile_size):
        super().__init__()
        self.piece_type = piece_type
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

# Add pieces to the sprite group based on the array
tile_size = SQUARE_SIZE  # Each tile is 110x110 pixels

for row in range(8):
    for col in range(8):
        piece = chessboard[row][col][0]
        if piece != 0:
            image_path = piece_images[piece]
            position = (200 + col * tile_size, 60 + row * tile_size)
            chess_piece = ChessPiece(piece, image_path, position, tile_size)
            chess_piece_group.add(chess_piece)

# Function to get the tile position from mouse position
def get_tile_pos(mouse_pos):
    x, y = mouse_pos
    return (x - 200) // tile_size, (y - 60) // tile_size

# Square class for drawing the board
class Square:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Create squares
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

# Game loop variables
selected_piece = None
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col, row = get_tile_pos(mouse_pos)
            if 0 <= row < 8 and 0 <= col < 8:  # Ensure the click is within the board
                if selected_piece is None:
                    # Select a piece
                    piece = chessboard[row][col][0]
                    if piece != 0:
                        selected_piece = (row, col, piece)
                        chessboard[row][col] = [0]  # Temporarily remove the piece from the board
                else:
                    # Move the selected piece
                    new_row, new_col = row, col
                    chessboard[new_row][new_col] = [selected_piece[2]]
                    selected_piece = None

                    # Update the sprite positions
                    chess_piece_group.empty()
                    for row in range(8):
                        for col in range(8):
                            piece = chessboard[row][col][0]
                            if piece != 0:
                                image_path = piece_images[piece]
                                position = (200 + col * tile_size, 60 + row * tile_size)
                                chess_piece = ChessPiece(piece, image_path, position, tile_size)
                                chess_piece_group.add(chess_piece)

    screen.fill((100, 150, 150))  # Clear screen with a background color

    # Draw the squares
    for row in squares:
        for square in row:
            square.draw(screen)

    # Update and draw the chess pieces
    chess_piece_group.update()
    chess_piece_group.draw(screen)

    pygame.display.update()

pygame.quit()
