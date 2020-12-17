from color import Color
from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    def __init__(self):
        self.matrix = [[None for i in range(8)] for j in range(8)]
        self.columns = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3, "F": 2, "G": 1, "H": 0}
        self.inv_col = {7: "A", 6: "B", 5: "C", 4: "D", 3: "E", 2: "F", 1: "G", 0: "H"}

    def initialize_pieces(self, color: Color):
        if color == Color.WHITE:
            i, j = 6, 7
        else:
            i, j = 1, 0
        # Initialize pawns
        for k in range(8):
            for letter in self.columns.keys():
                self.matrix[i][k] = Pawn(color, letter + str(i + 1))
                break
        # Rooks
        self.matrix[j][0] = Rook(color, "H" + str(j + 1))
        self.matrix[j][7] = Rook(color, "A" + str(j + 1))
        # Knights
        self.matrix[j][1] = Knight(color, "G" + str(j + 1))
        self.matrix[j][6] = Knight(color, "B" + str(j + 1))
        # Bishops
        self.matrix[j][2] = Bishop(color, "F" + str(j + 1))
        self.matrix[j][5] = Bishop(color, "C" + str(j + 1))
        # Royalty
        self.matrix[j][3] = Queen(color, "E" + str(j + 1))
        self.matrix[j][4] = King(color, "D" + str(j + 1))

    def __getitem__(self, pos: str) -> Piece:
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        return self.matrix[row][column]

    def __setitem__(self, pos: str, item: Piece):
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        self.matrix[row][column] = item

    def indeces_to_coordinates(self, i: int, j: int) -> str:
        row = str(i + 1)
        col = self.columns[j]
        return col + row
