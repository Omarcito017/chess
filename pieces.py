from color import Color
class Piece:
    def __init__(self, color: Color, i: int, j: int):
        self.color = color
        self.position = (i, j)
        self.firstMove = True

class Pawn(Piece):
    def valid_moves(self, board):
    
    def promote(self):

class Rook(Piece):
    def valid_moves(self, board):

class Knight(Piece):
    def valid_moves(self, board):

class Bishop(Piece):
    def valid_moves(self, board):

class Queen(Piece):
    def valid_moves(self, board):

class King(Piece):
    def valid_moves(self, board):