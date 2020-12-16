class Piece:
    def __init__(self, color: str, i: int, j: int):
        self.color = color
        self.position = (i, j)
        self.firstMove = True

    def valid_moves(
        self, board
    ):  # Returns a list of valid coordinates for respective piece
        pass

    def inside_board(self, i: int, j: int) -> bool:
        return 0 < i < 8 and 0 < j < 8


class Pawn(Piece):
    def valid_moves(self, board: list[list[Piece]]):
        i, j = self.position
        coordinates = []
        if self.color == Color.WHITE:
            op = lambda a, b: a + b
        else:
            op = lambda a, b: a - b
            # Check front moves
            if self.firstMove and not board[op(i, 2)][j]:
                coordinates.append(str((op(i, 2) + 1), str(board.inv_col[j])))
            if self.inside_board(op(i, 1), j) and not board[op(i, 1)][j]:
                coordinates.append((str(op(i, 1) + 1), str(board.inv_col[j])))
            # Check left diagonal
            if self.inside_board(op(i, 1), j - 1):
                if (
                    not board[op(i, 1)][j - 1]
                    or board[op(i, 1)][j - 1].color == Color.BLACK
                ):
                    coordinates.append((str(op(i, 1) + 1), str(board.inv_col[j - 1])))
            # Check right diagonal
            if self.inside_board(op(i, 1), j + 1):
                if (
                    not board[op(i, 1)][j + 1]
                    or board[op(i, 1)][j + 1].color == Color.BLACK
                ):
                    coordinates.append((str(op(i, 1) + 1), str(board.inv_col[j - 1])))
        return coordinates

    def promote(self):
        pass


class Rook(Piece):
    def valid_moves(self, board):
        pass


class Knight(Piece):
    def valid_moves(self, board):
        pass


class Bishop(Piece):
    def valid_moves(self, board):
        pass


class Queen(Piece):
    def valid_moves(self, board):
        pass


class King(Piece):
    def valid_moves(self, board):
        pass
