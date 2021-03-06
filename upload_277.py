from random import randint
import re
import sys
from typing import List, Tuple


NEIGHBORS: List[Tuple[int, int]] = [(-1, 1), (0, 1), (1, 1),
                                    (-1, 0), (1, 0),
                                    (-1, -1), (0, -1), (1, -1)]


def get_rules(rules: str) -> List[int]:
    """Takes formatted string of rules, returns a list of the rules as integers. Complexity: O(1)"""
    rules = re.findall(r'B(\d)\/S(\d)(\d)', rules)
    int_rules: List[int] = [int(rule) for rule in rules[0]]
    return int_rules


def initialize_board(size: int) -> List[List[int]]:
    """Takes an int for size and returns a board (list of lists) accordingly.
    Complexity: O(n^2)"""
    board = [[randint(0, 1) for _i in range(size)] for _i in range(size)]
    return board


def determine_cell(board: List[List[int]], x: int, y: int, counter, rules) -> int:
    """Takes the board, position parameters, and the number of living neighbors.
    Returns 1 if cell is alive 0 if dead. Complexity: O(1)"""
    if board[x][y] == 1:
        if rules[1] <= counter <= rules[2]:
            return 1
        if counter < rules[1] or counter > rules[2]:
            return 0
    elif counter == rules[0]:
        return 1
    else:
        return 0


def check_neighbor(board: List[List[int]], x: int, y: int, neighbor: Tuple[int, int]) -> int:
    """Takes the board, position parameters, and tuple for a relative neighbor position.
    Returns 1 if neighbor is alive 0 if dead. Complexity: O(1)"""
    try:
        return board[x + neighbor[0]][y + neighbor[1]]
    except IndexError:
        return 0


def check_cell(board: List[List[int]], x: int, y: int) -> int:
    """Takes a board and position parameters.
    Returns an integer with the number of living neighboring cells. Complexity: O(1)"""
    counter = 0
    if board[x][y] == 1:
        for neighbor in NEIGHBORS:
            counter += check_neighbor(board, x, y, neighbor)
    return counter


def generation(board: List[List[int]], rules) -> List[List[int]]:
    """Takes a board and returns another board according to the generation rules. Complexity: O(N)"""
    tng = [[0 for _i in range(len(board))] for _i in range(len(board))]
    for x, line in enumerate(board):
        for y, _cell in enumerate(line):
            counter = check_cell(board, x, y)
            state = determine_cell(board, x, y, counter, rules)
            tng[x][y] = state
    return tng


def print_board(board: List[List[int]]) -> str:
    """Takes the board. Returns a formatted printout string of the board. Complexity: O(N^2)"""
    printout = ''
    for x, line in enumerate(board):
        printout += '\n'
        for y, _cell in enumerate(line):
            if board[x][y] == 1:
                printout += '░'
            else:
                printout += ' '
    printout += '\n'
    return printout


def run_game(generations: str, size: str, rule: str):
    """Takes number of generations, board size, and rules and runs the game. Complexity: O(N^2)"""
    generations = int(generations)
    size = int(size)
    rules = get_rules(rule)
    board = initialize_board(size)
    print('-' * size)
    for _i in range(generations):
        board = generation(board, rules)
        print(print_board(board))
        print('-' * size)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        run_game(sys.argv[1], sys.argv[2], sys.argv[3])
    if len(sys.argv) == 3:
        run_game(sys.argv[1], sys.argv[2], 'B3/S23')
