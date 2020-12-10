from color import Color
from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King
class Board:
    def __init__(self):
        self.matrix = [[None for i in range(8)] for j in range(8)]
        self.columns = {
            'A': 7,
            'B': 6,
            'C': 5,
            'D': 4,
            'E': 3,
            'F': 2,
            'G': 1,
            'H': 0
        }
    def initialize_pieces(self, color: Color):
        if color == Color.WHITE:
            i, j = 6, 7
        else:
            i, j = 1, 0
        #Initialize pawns
        for k in range(8):
            for letter in self.columns.keys():
                self.matrix[i][k] = Pawn(color, str(i + 1), letter)
                break
        #Rooks
        self.matrix[j][0] = Rook(color, str(j + 1), 'H')
        self.matrix[j][7] = Rook(color, str(j + 1), 'A')
        #Knights
        self.matrix[j][1] = Knight(color, str(j + 1), 'G')
        self.matrix[j][6] = Knight(color, str(j + 1), 'B')
        #Bishops
        self.matrix[j][2] = Bishop(color, str(j + 1), 'F')
        self.matrix[j][5] = Bishop(color, str(j + 1), 'C')
        #Royalty
        self.matrix[j][3] = Queen(color, str(j + 1), 'E')
        self.matrix[j][4] = King(color, str(j + 1), 'D')
    
    def __getitem__(self, pos: str) -> Piece:
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        return self.matrix[row][column]
    
    def __setitem__(self, pos: str, item: Piece):
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        self.matrix[row][column] = item



