import pieces
import numpy as np


class Game:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.initialize_white()
        self.initialize_black()

    def in_check(self) -> bool:
        pass

    def in_checkmate(self) -> bool:
        pass
