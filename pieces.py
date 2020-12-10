from color import Color
class Piece:
    def __init__(self, color: Color, row: str, column: str):
        self.color = color
        self.position = (row, column)
        self.firstMove = True
    def valid_moves(self):
        pass

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