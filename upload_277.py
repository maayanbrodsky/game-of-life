from random import randint
import sys
from typing import List, Tuple


NEIGHBORS: List[Tuple[int, int]] = [(-1, 1), (0, 1), (1, 1),
             (-1, 0), (1, 0),
             (-1, -1), (0, -1), (1, -1)]


def intialize_board(size: int) -> List[List[int]]:
    """Takes an int for size and returns a board (list of lists) accordingly."""
    board = [[randint(0, 1) for i in range(size)] for i in range(size)]
    return board


def determine_cell(board: List[List[int]], x: int, y: int, counter) -> int:
    """Takes the board, position parameters, and the number of living neighbors.
    Returns 1 if cell is alive 0 if dead."""
    if board[x][y] == 1 and 2 <= counter <= 3:
        return 1
    if board[x][y] == 1 and 2 > counter > 3:
        return 0
    if board[x][y] == 0 and counter == 3:
        return 1
    else:
        return 0


def check_neighbor(board: List[List[int]], x: int, y: int, neighbor: Tuple[int, int]) -> int:
    """Takes the board, position parameters, and tuple for a relative neighbor position.
    Returns 1 if neighbor is alive 0 if dead."""
    increment = 0
    try:
        if board[x + neighbor[0]][y + neighbor[1]] == 1:
            increment += 1
    except IndexError:
        pass
    return increment


def check_cell(board: List[List[int]], x: int, y: int) -> int:
    """Takes a board and position parameters.
    Returns an integer with the number of living neighboring cells."""
    counter = 0
    if board[x][y] == 1:
        for neighbor in NEIGHBORS:
            counter += check_neighbor(board, x, y, neighbor)
    return counter


def generation(board: List[List[int]]) -> List[List[int]]:
    """Takes a board and returns another board according to the generation rules."""
    tng = [[0 for i in range(len(board))] for i in range(len(board))]
    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            counter = check_cell(board, x, y)
            state = determine_cell(board, x, y, counter)
            tng[x][y] = state
    return tng


def print_board(board: List[List[int]], size: int) -> str:
    """Takes the board and board size. Returns a formatted printout string of the board."""
    printout = ''
    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            if y == size - 1 and board[x][y] == 1:
                printout += '░\n'
            elif y == size - 1 and board[x][y] == 0:
                printout += ' \n'
            elif board[x][y] == 1:
                printout += '░'
            else:
                printout +=' '
    return printout


def run_game(generations: str, size: str):
    """Takes number of generations and board size and runs the game."""
    generations = int(generations)
    size = int(size)
    board = intialize_board(size)
    print('-' * size)
    for i in range(generations):
        board = generation(board)
        print(print_board(board, size))
        print('-' * size)


if __name__ == '__main__':
    run_game(sys.argv[1], sys.argv[2])
