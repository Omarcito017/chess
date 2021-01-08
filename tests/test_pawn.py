from chess.game import Game

"""Pawn Moves Test"""


def test_indices_to_position():
    state = Game()
    i, j = 6, 3
    result = state.board.idxs_to_position(i, j)
    assert result == "E7"


def test_forward():
    state = Game()
    for col in state.board.columns.keys():
        position = col + str(7)
        result = state.board.valid_moves(position)
        assert len(result) == 2
        assert col + str(6) in result
        assert col + str(5) in result


def test_front_and_diagonal():
    state = Game()
    rook = state.board["H1"]
    state.board["G6"] = rook
    result1 = state.board.valid_moves("F7")
    result2 = state.board.valid_moves("H7")
    assert len(result1) == 3 and len(result2) == 3
    assert "G6" in result1
    assert "G6" in result2
    assert "F6" in result1 and "H6" in result2
    assert "F5" in result1 and "H5" in result2
