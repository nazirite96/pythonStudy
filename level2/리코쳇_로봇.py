import collections


def solution(board):
    answer = -1
    x_ren = len(board[0])
    y_ren = len(board)
    for y,line in enumerate(board):
        if 'R' in line:
            r_x, r_y = line.index('R'), y
        if 'G' in line:
            g_x, g_y = line.index('G'), y
    directions = {'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}
    visited_xy = [(r_x,r_y)]
    deque = collections.deque()
    deque.append([r_x, r_y, 0])
    find_answer = False
    while deque and not find_answer:
        case_info = deque.popleft()
        x, y, count = case_info[0], case_info[1], case_info[2]

        count += 1
        for direct in directions.keys():
            next_x,next_y = x,y
            dx,dy = directions[direct]
            while 0 <= next_x+dx < x_ren and 0 <= next_y+dy < y_ren and board[next_y+dy][next_x+dx] != 'D':
                next_x += dx
                next_y += dy
            if (next_x,next_y) not in visited_xy:
                deque.append([next_x,next_y,count])
                visited_xy.append((next_x,next_y))
            if next_x == g_x and next_y == g_y:
                answer = count
                find_answer = True

    return answer



board = ["...D..R",
         ".D.G...",
         "....D.D",
         "D....D.",
         "..D...."]

print(solution(board))

board =[".D.R", "....", ".G..", "...D"]
print(solution(board))