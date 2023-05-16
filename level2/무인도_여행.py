maps_bool_list = []
import sys
sys.setrecursionlimit(100000)

def solution(maps):
    answer = []
    global maps_bool_list
    str_s = 's'
    str_s.upper()
    for map in maps:
        list = [char.isdigit() for char in map]
        maps_bool_list.append(list)
    for y,line in enumerate(maps_bool_list):
        for x,box in enumerate(line):
            if box:
                count = bfs(maps, y, x, 0)
                answer.append(count)

    if len(answer) == 0 :
        answer.append(-1)
    answer.sort()
    return answer

def bfs(maps, y, x,count):
    global maps_bool_list
    maps_bool_list[y][x] = False
    count += int(maps[y][x])
    # up
    if(y-1 >= 0 and maps_bool_list[y-1][x]):
        count = bfs(maps, y-1, x, count)
    # right
    if(x+1 < len(maps[0])and maps_bool_list[y][x+1]):
        count = bfs(maps, y, x+1, count)
    # down
    if(y+1 < len(maps) and maps_bool_list[y+1][x]):
        count = bfs(maps, y+1, x, count)
    # left
    if(x-1 >= 0 and maps_bool_list[y][x-1]):
        count = bfs(maps, y, x-1, count)

    return count


maps = ["X591X",
        "X1X5X",
        "X231X",
        "1XXX1"]

print(solution(maps))

