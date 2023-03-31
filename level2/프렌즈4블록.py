def solution(m, n, board):
    global answer
    answer = 0
    board_list = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(board[j][i])
        board_list.append(line)

    while True:
        can_removed = check_can_removed(m, n, board_list)
        if len(can_removed) == 0:
            break
        removed_block(can_removed,board_list)
        falling_blocks(board_list)

    print(board_list)
    # [' ', ' ', ' ', ' '],
    # [' ', ' ', ' ', ' '],
    # ['B', 'B', ' ', ' '],
    # ['D', 'D', 'B', 'B'],
    # ['E', 'E', 'F', 'F']]
    [[],
     [],
     ['B', 'B'],
     ['D', 'D', 'B', 'B'],
     ['E', 'E', 'F', 'F']]
    return answer


def check_can_removed(m, n, board_list):
    coordinate = []
    for x in range(n-1):
        for y in range(len(board_list[x]) - 1):
            if board_list[x][y] != ' ' and board_list[x][y] == board_list[x + 1][y] == board_list[x][y + 1] == board_list[x + 1][y + 1]:
                coordinate.append(x)
                coordinate.append(y)
    return coordinate


def removed_block(coordinate,board_list):
    for i in range(0,len(coordinate),2):
        x = coordinate[i] # x
        y = coordinate[i+1] # y
        board_list[x][y], board_list[x+1][y] = '*','*'
        board_list[x][y+1], board_list[x+1][y+1] = '*','*'

def falling_blocks(board_list):
    global answer
    for board in board_list:
        i = 0
        while True:
            k = len(board)
            if i == k:
                break
            if board[i] == '*':
                answer += 1
                board.pop(i)
                board.insert(0,' ')
            else:
                i+=1




print(solution(4, 5, ["CCBDE",
                      "AAADE",
                      "AAABF",
                      "CCBBF"]))
