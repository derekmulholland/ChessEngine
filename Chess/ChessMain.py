"""
Driver file. Responsible for handling user input and displaying current GameState Object
"""

import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations
IMAGES = {}

"""
Initialize a global dictionary of images. This weill be called exactly once in main
"""
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: access an image by saying 'IMAGES['wp']'


"""
Main Driver for the code. Handles user input and updating graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # only done once before while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
Responsible for graphics in current game state.
"""
def drawGameState(screen, gs):
    drawBoard(screen)  # draws squares on the board
    # FIXME: add in piece highlighting or move suggestions
    drawPieces(screen, gs.board)  # draw pieces on top of squares.


"""
Draw squares on the board, the top left is always light.
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("brown")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw Pieces on the current GameState.board
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # non empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
