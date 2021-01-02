from upload_277 import initialize_board, determine_cell, check_neighbor, check_cell, generation, print_board


def test_initialize_board():
    board = initialize_board(4)
    assert len(board) == 4
    assert len(board[0]) == 4


def test_determine_cell():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert determine_cell(board, 1, 1, 4) == 0


def test_check_neighbor():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert check_neighbor(board, 1, 1, (0, 1)) == 0


def test_check_cell():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert check_cell(board, 1, 1) == 0


def test_generation():
    board = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert generation(board) == [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert generation(board) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def test_print_board():
    board = [[0, 1], [0, 0]]
    assert print_board(board) == '\n ░\n  \n'
