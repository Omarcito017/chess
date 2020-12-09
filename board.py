from color import Color
import pieces
class Board:
    def __init__(self):
        self.matrix = [[None for i in range(8)] for j in range(8)]
    def initialize_pieces(self, color: Color):
        if color == Color.WHITE:
            i, j = 6, 7
        else:
            i, j = 1, 0
        #Initialize pawns
        for k in range(8):
            self.matrix[i][k] = pieces.Pawn(color, i, k)
        #Rooks
        self.matrix[j][0] = pieces.Rook(color, j, 0)
        self.matrix[j][7] = pieces.Rook(color, j, 7)
        #Knights
        self.matrix[j][1] = pieces.Knight(color, j, 1)
        self.matrix[j][6] = pieces.Knight(color, j, 6)
        #Bishops
        self.matrix[j][2] = pieces.Bishop(color, j, 2)
        self.matrix[j][5] = pieces.Bishop(color, j, 5)
        #Royalty
        self.matrix[j][3] = pieces.Queen(color, j, 3)
        self.matrix[j][4] = pieces.King(color, j, 4)