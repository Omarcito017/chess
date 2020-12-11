from board import Board
from color import Color


class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_pieces(Color.WHITE)
        self.board.initialize_pieces(Color.BLACK)
