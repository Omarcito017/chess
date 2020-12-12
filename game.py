import pieces
import numpy as np

class Game():
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.initialize_white()
        self.initialize_black()
    
    def initialize_white(self):
        #Initialize pawns
        for j in range(8):
            self.board[6][j] = pieces.Pawn('w', 6, j)
        #Rooks
        self.board[7][0] = pieces.Rook('w', 7, 0)
        self.board[7][7] = pieces.Rook('w', 7, 7)
        #Knights
        self.board[7][1] = pieces.Knight('w', 7, 1)
        self.board[7][6] = pieces.Knight('w', 7, 6)
        #Bishops
        self.board[7][2] = pieces.Bishop('w', 7, 2)
        self.board[7][5] = pieces.Bishop('w', 7, 5)
        #Royalty
        self.board[7][3] = pieces.Queen('w', 7, 3)
        self.board[7][4] = pieces.King('w', 7, 4)
    
    def initialize_black(self):
        #Initialize pawns
        for j in range(8):
            self.board[1][j] = pieces.Pawn('b', 1, j)
        #Rooks
        self.board[0][0] = pieces.Rook('b', 0, 0)
        self.board[0][7] = pieces.Rook('b', 0, 7)
        #Knights
        self.board[0][1] = pieces.Knight('b', 0, 1)
        self.board[0][6] = pieces.Knight('b', 0, 6)
        #Bishops
        self.board[0][2] = pieces.Bishop('b', 0, 2)
        self.board[0][5] = pieces.Bishop('b', 0, 5)
        #Royalty
        self.board[0][3] = pieces.Queen('b', 0, 3)
        self.board[0][4] = pieces.King('b', 0, 4)

    def in_check(self) -> bool:
        pass

    def in_checkmate(self) -> bool:
        pass


