# import math
# def check_square(x,y,n,board):
#     for i in range(0, n ):
#         if 0 in board[y+i][x:x+n]:
#             return False
#     return True
#
# def solution(board):
#     answer = 0
#
#     count_one = sum([line.count(1) for line in board])
#     print(count_one)
#     max_n = int(math.sqrt(count_one))
#     check_flag = False
#     for n in range(max_n,0,-1):
#         for y in range(0, len(board)-n+1):
#             for x in range(0,len(board[0])-n+1):
#                 check_flag = square = check_square(x, y, n, board)
#                 if check_flag:
#                     break
#             if check_flag:
#                 break
#         if check_flag:
#             answer = n * n
#             break
#     return answer

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


[[0, 1, 1, 1],
 [1, 1, 2, 2],
 [1, 2, 2, 3],
 [0, 0, 1, 0]]