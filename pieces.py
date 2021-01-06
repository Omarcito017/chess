from color import Color
from abc import ABC


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color
        self.firstMove = True


class Pawn(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass
