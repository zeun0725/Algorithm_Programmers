# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679#


def rm_block(m, n, board):
    count = 0
    values = [[0] * n for _ in range(m)]
    for i, x in enumerate(board[:-1]):
        for j, y in enumerate(x[:-1]):
            if x[j] == x[j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '':
                values[i][j] = 1
                values[i][j + 1] = 1
                values[i + 1][j] = 1
                values[i + 1][j + 1] = 1
    for i in range(m):
        for j in range(n):
            if values[i][j] == 1:
                count += 1
    return values, count

def rm_board(values, board, m, n):
    for i in range(m):
        for j in range(n):
            if values[i][j] == 1:
                board[i][j] = ''
    board2 = list(zip(*board))
    for i, b in enumerate(board2):
        add_block = ''.join(b)
        board2[i] = [''] * (m - len(add_block)) + list(add_block)
    return list(map(list, zip(*board2)))


def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    count = -1
    while count != 0:
        rm_values, count = rm_block(m, n, board)
        board = rm_board(rm_values, board, m, n)
        answer += count
    return answer