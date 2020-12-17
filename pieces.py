from color import Color
from board import Board
from abc import ABC


class Piece(ABC):
    def __init__(self, color: Color, position: str):
        self.color = color
        self.position = position
        self.firstMove = True

    def valid_moves(self, board: Board):
        pass

    def inside_board(self, i: int, j: int):
        return 0 < i < 8 and 0 < j < 8


class Pawn(Piece):
    def valid_moves(self, board: Board):
        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b

        # Integer values to index the matrix
        i, j = board.coordinates_to_indeces(self.position)
        coordinates = []
        if self.color == Color.WHITE:
            op = add
        else:
            op = sub
        # Check front moves
        if self.firstMove and not board.matrix[op(i, 2)][j]:
            coordinates.append(board.indeces_to_coordinates(op(i, 2), j))
        if self.inside_board(op(i, 1), j) and not board.matrix[op(i, 1)][j]:
            coordinates.append(board.indeces_to_coordinates(op(i, 1), j))
        # Check Left Diagonal
        if self.inside_board(op(i, 1), j - 1) and board.matrix[op(i, 1)][j - 1]:
            if board.matrix[op(i, 1)][j - 1].color != self.color:
                coordinates.append(board.indeces_to_coordinates(op(i, 1), j - 1))
        # Check Right Diagonal
        if self.inside_board(op(i, 1), j + 1) and board.matrix[op(i, 1)][j + 1]:
            if board.matrix[op(i, 1)][j + 1].color != self.color:
                coordinates.append(board.indeces_to_coordinates(op(i, 1), j + 1))
        return coordinates


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
