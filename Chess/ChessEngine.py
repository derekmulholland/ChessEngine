"""
Storing information about the current state of a chess game. Also responsible for determining valid
moves at the current state. It will also keep a move log.
"""


class GameState():
    def __init__(self):
        # 8x8 board is a 2D list, each list element is 2 characters.
        # first character is the color, 'b'-black, 'w'-white
        # second character is the piece type:
        # 'p'-pawn, 'R'-rook, 'N'-knight, 'B'-bishop, 'Q'-queen, 'K'-king
        # '--' represents empty space that does not have a piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

