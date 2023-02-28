def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                not_safe_zone_check(board, i, j, n)
    print(board)
    for line in board:
        answer += line.count(0)

    return answer

def not_safe_zone_check(board,i,j,n):
    left = int(j - 1 >= 0)
    right = int(j + 1 != n)
    up = int(i - 1 >= 0)
    down = int(i + 1 != n)
    if board[i][j-left] != 1:
        board[i][j-left] = 9
    if board[i][j+right] != 1:
        board[i][j+right] = 9
    if board[i-up][j] != 1:
        board[i-up][j] = 9
    if board[i+down][j] != 1:
        board[i+down][j] = 9
    if board[i-up][j-left] != 1:
        board[i-up][j-left] = 9
    if board[i+down][j-left] != 1:
        board[i+down][j-left] = 9
    if board[i+down][j+right] != 1:
        board[i+down][j+right] = 9
    if board[i-up][j-left] != 1:
        board[i-up][j-left] = 9
    if board[i-up][j+right] != 1:
        board[i-up][j+right] = 9






board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

print(solution(board))