from color import Color
from board import Board
from abc import ABC


class Piece(ABC):
    def __init__(self, color: Color, position: str):
        self.color = color
        self.position = position
        self.firstMove = True

    def valid_moves(self, board):
        pass

    def inside_board(self, i: int, j: int):
        return 0 < i < 8 and 0 < j < 8


class Pawn(Piece):
    def valid_moves(self, board: Board):
        pass


class Rook(Piece):
    def valid_moves(self):
        pass


class Knight(Piece):
    def valid_moves(self):
        pass


class Bishop(Piece):
    def valid_moves(self):
        pass


class Queen(Piece):
    def valid_moves(self):
        pass


class King(Piece):
    def valid_moves(self):
        pass
