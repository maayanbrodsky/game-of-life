from random import randint
from typing import List


NEIGHBORS = [(-1, 1), (0, 1), (1, 1),
             (-1, 0), (1, 0),
             (-1, -1), (0, -1), (1, -1)]


def intialize_board(size):
    board = [[randint(0, 1) for i in range(size)] for i in range(size)]
    return board


def generation(board: List[List[int]]):
    for x, line in enumerate(board):
        for y, cell in enumerate(line):
            # print(x, y, cell)
            check_cell(x, y, board)



def check_cell(x, y, board):
    counter = 0
    if board[x][y] == 1:
        for neighbor in NEIGHBORS:
            counter += check_neighbor(board, x, y, neighbor)
    print(f'cell: ({x}, {y}) is in state: {board[x][y]} and has {counter} living neighbors.')


def check_neighbor(board, x, y, neighbor):
    increment = 0
    try:
        if board[x + neighbor[0]][y + neighbor[1]] == 1:
            increment += 1
    except IndexError:
        pass
    return increment


board = intialize_board(50)
generation(board)

# print(*board, sep='\n')
