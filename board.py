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
            self.matrix[i][k] = Pawn(color)

        # Rooks
        self.matrix[j][0] = Rook(color)
        self.matrix[j][7] = Rook(color)
        # Knights
        self.matrix[j][1] = Knight(color)
        self.matrix[j][6] = Knight(color)
        # Bishops
        self.matrix[j][2] = Bishop(color)
        self.matrix[j][5] = Bishop(color)
        # Royalty
        self.matrix[j][3] = Queen(color)
        self.matrix[j][4] = King(color)

    def __getitem__(self, pos: str) -> Piece:
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        return self.matrix[row][column]

    def __setitem__(self, pos: str, item: Piece):
        row = int(pos[1]) - 1
        column = self.columns[pos[0]]
        self.matrix[row][column] = item

    def inside_board(self, i: int, j: int):
        return 0 <= i < 8 and 0 <= j < 8

    def indeces_to_coordinates(self, i: int, j: int) -> str:
        row = str(i + 1)
        col = self.inv_col[j]
        print(col + row)
        return col + row

    def coordinates_to_indeces(self, coord: str) -> tuple:
        i, j = int(coord[1]) - 1, self.columns[coord[0]]
        return (i, j)

    def valid_moves(self, position: str) -> list[str]:
        curr_piece = self[position]
        print("Good")
        if isinstance(curr_piece, Pawn):
            print("Went inside")
            return self.pawn_valid_moves(position, curr_piece)

    def pawn_valid_moves(self, position: str, curr_piece: Piece) -> list[str]:
        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b
        print("got called")
        # Integer values to index the matrix
        i, j = self.coordinates_to_indeces(position)
        coordinates = []
        if curr_piece.color == Color.WHITE:
            op = sub
        else:
            op = add
        # Check front moves
        if curr_piece.firstMove and not self.matrix[op(i, 2)][j]:
            coordinates.append(self.indeces_to_coordinates(op(i, 2), j))
        if self.inside_board(op(i, 1), j) and not self.matrix[op(i, 1)][j]:
            coordinates.append(self.indeces_to_coordinates(op(i, 1), j))
        # Check Left Diagonal
        if self.inside_board(op(i, 1), j - 1) and self.matrix[op(i, 1)][j - 1]:
            if self.matrix[op(i, 1)][j - 1].color != curr_piece.color:
                coordinates.append(self.indeces_to_coordinates(op(i, 1), j - 1))
        # Check Right Diagonal
        if self.inside_board(op(i, 1), j + 1) and self.matrix[op(i, 1)][j + 1]:
            if self.matrix[op(i, 1)][j + 1].color != curr_piece.color:
                coordinates.append(self.indeces_to_coordinates(op(i, 1), j + 1))
        print(coordinates)
        return coordinates
