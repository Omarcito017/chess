from abc import ABC

from chess.color import Color


class Piece(ABC):
    """The class Piece represents each piece in Chess."""

    def __init__(self, color: Color):
        self.color = color
        self.first_move = True


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
