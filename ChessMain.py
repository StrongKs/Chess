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
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f"venv/images/{piece}.png"), (SQ_SIZE, SQ_SIZE))
    #   Note: we can access an image by using 'IMAGES'


"""
The main driver for our code. This will handle user input and updating the graphics
"""


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Practice", "icon")
    icon = pygame.image.load(f"venv/images/bK.png").convert()
    pygame.display.set_icon(icon)   # set window icon
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gameState = ChessEngine.GameState()
    loadImages()  # only do this once, before the while loop
    running = True
    sqSelected = ()    # no square is selected, keep track of the last click of the user (tuple: (row, col))
    playerClicks = []   # keep track of player clicks (two tuples: [(6, 4), (4, 4)])
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()   # (x, y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):   # user clicked the same square twice
                    sqSelected = ()    # deselected
                    playerClicks = {}    # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)    # append for both 1st and 2nd clicks
                if len(playerClicks) == 2:    # after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gameState.board)
                    print(move.getChessNotation())
                    gameState.makeMove(move)
                    sqSelected = ()   # reset user clicks
                    playerClicks = []

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
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":   # not empty  square
                screen.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
