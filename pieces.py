from color import Color
from abc import ABC

class Piece(ABC):
    def __init__(self, color: Color, row: str, column: str):
        self.color = color
        self.position = (row, column)
        self.firstMove = True

    @abstractmethod
    def valid_moves(self):
        pass


class Pawn(Piece):
    def valid_moves(self):
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
