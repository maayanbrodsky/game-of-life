from upload_277 import check_cell, check_neighbor, determine_cell, generation, initialize_board, print_board


def test_initialize_board():
    board = initialize_board(4)
    assert len(board) == 4
    assert len(board[0]) == 4


def test_determine_cell():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert determine_cell(board, 1, 1, 4, (3, 2, 3)) == 0


def test_check_neighbor():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert check_neighbor(board, 1, 1, (0, 1)) == 0


def test_check_cell():
    board = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert check_cell(board, 1, 1) == 0


def test_generation():
    board = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert generation(board, (3, 2, 3)) == [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert generation(board, (3, 2, 3)) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def test_print_board():
    board = [[0, 1], [0, 0]]
    assert print_board(board) == '\n ░\n  \n'
