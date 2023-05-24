def solution(board):
    width = len(board[0])
    height = len(board)
    for y in range(1, height):
        for x in range(1, width):
            if board[y][x] == 1:
                board[y][x] = min(board[y-1][x-1], board[y-1][x], board[y][x-1]) + 1

    print(board)
    return max([item for sublist in board for item in sublist]) ** 2

print(solution([[0,0,1,1],[1,1,1,1]]))
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
