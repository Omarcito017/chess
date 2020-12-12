class Piece:
    def __init__(self, color: str, i: int, j: int):
        self.color = color
        self.position = (i, j)
        self.firstMove = True
    def valid_moves(self, board): #Returns a list of valid coordinates for respective piece
        pass
    def inside_board(self, i: int, j: int) -> bool:
        if square[0] < 8 and suare[1] < 8:
            return True
        return False

class Pawn(Piece):
    def valid_moves(self, board: list[list[Piece]]):
        i, j = self.position  
        coordinates = []          
        if self.color == 'w':
            #Check front moves
            if self.firstMove and not board[i + 2][j]:
                coordinates.append((i + 2, j))
            if self.insideBoard((i + 1, j)) and not board[i + 1][j]:
                coordinates.append((i + 1, j))
            #Check left diagonal
            if self.insideBoard(i + 1, j - 1):
                if not board[i + 1][j - 1] or board[i + 1][j - 1].color == 'b':
                    coordinates.append((i + 1, j - 1))
            #Check right diagonal
            if self.insideBoard(i + 1, j + 1):
                if not board[i + 1][j + 1] or board[i + 1][j + 1].color == 'b':
                    coordinates.append((i + 1, j - 1))
        else:
            #Check front moves
            if self.firstMove and not board[i - 2][j]:
                coordinates.append((i - 2, j))
            if self.insideBoard((i - 1, j)) and not board[i - 1][j]:
                coordinates.append((i - 1, j))
            #Check left diagonal
            if self.insideBoard(i - 1, j + 1):
                if not board[i - 1][j + 1] or board[i - 1][j + 1].color == 'w':
                    coordinates.append((i - 1, j + 1))
            #Check right diagonal
            if self.insideBoard(i - 1, j - 1):
                if not board[i - 1][j - 1] or board[i - 1][j - 1].color == 'w':
                    coordinates.append((i - 1, j - 1))
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
