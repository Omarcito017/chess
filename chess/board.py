from typing import List, Optional, Tuple

from chess.color import Color
from chess.pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook


def check_position_format(pos: str) -> None:
    """Asserts that the given position is valid on the chess board.

    Args:
            pos: Position on the chess board. The format of the string is
                f"{letter}{number}", e.g. "A7".
    """
    if len(pos) != 2:
        raise ValueError(
            "Valid Positions contain two characters: A letter and a number."
        )
    if pos[0] not in Board.columns.keys():
        raise ValueError("The first character must be a letter.")
    if not pos[1].isdigit() or int(pos[1]) not in range(1, 9):
        raise ValueError("The second character must be an integer in [1,8].")


class Board:
    """Board represents the chess board where the chess pieces move on."""

    # Mapping from Letters to Numbers for decoding Positions
    columns = {"A": 7, "B": 6, "C": 5, "D": 4, "E": 3, "F": 2, "G": 1, "H": 0}
    inv_cols = {v: k for k, v in columns.items()}

    def __init__(self):
        """Initializes an empty board with no pieces."""
        self.matrix = [[None for i in range(8)] for j in range(8)]

    def initialize_pieces(self, color: Color) -> None:
        """Creates starting pieces in starting positions for a certain color.

        Args:
            color: Color enum representing White or Black pieces
        """
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

    def __getitem__(self, pos: str) -> Optional[Piece]:
        """
        Args:
            pos: Position on the chess board. The format of the string is
                f"{letter}{number}", e.g. "A7".

        Returns:
            The Piece at the position on the Board
        """
        check_position_format(pos)
        row = int(pos[1]) - 1
        column = Board.columns[pos[0]]
        return self.matrix[row][column]

    def __setitem__(self, pos: str, piece: Piece) -> None:
        """
        Args:
            pos: Position on the chess board. The format of the string is
                f"{letter}{number}", e.g. "A7".
            piece: the Piece to put on the board
        """
        check_position_format(pos)
        row = int(pos[1]) - 1
        column = Board.columns[pos[0]]
        self.matrix[row][column] = piece

    def inside_board(self, i: int, j: int) -> bool:
        """Returns whether the indices are valid positions on the board"""
        assert isinstance(i, int) and isinstance(j, int)
        return 0 <= i < 8 and 0 <= j < 8

    def idxs_to_position(self, i: int, j: int) -> str:
        """Given a set of matrix indices, turn them into a Chess position.

        Args:
            i,j : Indices representing the chess Board

        Returns:
            corresponding Chess Postion, e.g. "A7"

        """
        row = str(i + 1)
        col = Board.inv_cols[j]
        pos = f"{col}{row}"
        check_position_format(pos)
        return pos

    def position_to_idxs(self, pos: str) -> Tuple[int, int]:
        """Converts Position to matrix indices.

        Args:
            pos: Position on the chess board. The format of the string is
                f"{letter}{number}", e.g. "A7".

        Returns:
            Tuple of matrix indices
        """
        check_position_format(pos)
        i, j = int(pos[1]) - 1, Board.columns[pos[0]]
        return (i, j)

    def valid_moves(self, pos: str) -> List[str]:
        """Returns all of the valid moves of a Piece at a given Position.

        Args:
            pos: Position on the chess board. The format of the string is
                f"{letter}{number}", e.g. "A7".

        Returns:
            List of valid positions the Piece at the given Position can move
        """
        curr_piece = self[pos]
        moves = []
        if isinstance(curr_piece, Pawn):
            moves = self._pawn_valid_moves(pos)
        return sorted(moves)

    def _pawn_valid_moves(self, pos: str) -> List[str]:
        """Returns all of the valid moves of a Pawn piece given a position.

        Args:
             pos: Position on the chess board. The format of the string is
                 f"{letter}{number}", e.g. "A7".

         Returns:
             List of valid positions the Pawn at the given Position can move
        """

        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b

        curr_piece = self[pos]
        # Integer values to index the matrix
        i, j = self.position_to_idxs(pos)
        positions = []

        # We can derive the logic for moving pieces forward or backward (add or subtract) based
        # on the color of the piece.
        op = sub if curr_piece.color == Color.WHITE else add

        # Add valid front moves
        if curr_piece.first_move and not self.matrix[op(i, 2)][j]:
            positions.append(self.idxs_to_position(op(i, 2), j))
        if self.inside_board(op(i, 1), j) and not self.matrix[op(i, 1)][j]:
            positions.append(self.idxs_to_position(op(i, 1), j))
        # Add valid Left Diagonal move
        if self.inside_board(op(i, 1), j - 1) and self.matrix[op(i, 1)][j - 1]:
            if self.matrix[op(i, 1)][j - 1].color != curr_piece.color:
                positions.append(self.idxs_to_position(op(i, 1), j - 1))
        # Add Right Diagonal move
        if self.inside_board(op(i, 1), j + 1) and self.matrix[op(i, 1)][j + 1]:
            if self.matrix[op(i, 1)][j + 1].color != curr_piece.color:
                positions.append(self.idxs_to_position(op(i, 1), j + 1))
        return positions
