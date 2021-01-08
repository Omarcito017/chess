import pytest

from chess import pieces
from chess.board import Board, check_position_format
from chess.game import Game


def test_check_position_format():
    with pytest.raises(ValueError):
        check_position_format("A77")
    with pytest.raises(ValueError):
        check_position_format("A9")
    with pytest.raises(ValueError):
        check_position_format("77")


def test_board_getitem():
    state = Game()

    assert isinstance(state.board["A7"], pieces.Pawn)
    assert state.board["D5"] is None


def test_board_setitem():
    state = Game()

    state.board["G6"] = state.board["H1"]
    assert state.board["G6"] == state.board["H1"]


def test_inside_board():
    board = Board()

    with pytest.raises(AssertionError):
        board.inside_board("A", "D")

    assert board.inside_board(0, 0)
    assert not board.inside_board(0, -1)


def test_position_to_idxs():
    board = Board()
    assert board.position_to_idxs("A7") == (6, 7)


def test_idxs_to_position():
    state = Game()
    result = state.board.idxs_to_position(6, 3)
    assert result == "E7"


def test_valid_moves():
    state = Game()

    pawn_moves = state.board.valid_moves("A7")
    assert pawn_moves == ["A5", "A6"]


def test_pawn_valid_moves():
    state = Game()

    first_moves = state.board._pawn_valid_moves("A7")
    assert first_moves == ["A5", "A6"]

    state.board["A7"].first_move = False
    after_first_moves = state.board._pawn_valid_moves("A7")
    assert after_first_moves == ["A6"]

    # move rook so Pawn can capture
    state.board["G6"] = state.board["H1"]
    capture_moves = state.board._pawn_valid_moves("F7")
    assert capture_moves == ["F5", "F6", "G6"]
