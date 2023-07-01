"""
This is our main driver file. It will be responsible for handling user input and display the current GameState object.
"""

import pygame
import ChessEngine

WIDTH = HEIGHT = 512  # 400 is another option
DIMENSION = 8  # dimension of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}


"""
Initialize a global dictionary of a image. This will be called exactly once in the main
"""


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load(f"venv/images/{piece}.png"), (SQ_SIZE, SQ_SIZE)
    #   Note: we can access an image by using 'IMAGES'


"""
The main driver for our code. This will handle user input and updating the graphics
"""


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gameState = ChessEngine.GameState()
    loadImages()  # only do this once, before the while loop
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        pygame.display.flip()


'''
Responsible for all the graphics within a current game state.
'''


def drawGameState(screen, gameState):
    drawBoard(screen)  # draw squares on the board
    # add in pieces highlighting or move suggestions (later)
    drawPieces(screen, gameState.board)


'''
Draw the squares on the board.
'''


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using the current GameState.board
'''


def drawPieces(screen, board):
    pass


if __name__ == "__main__":
    main()
