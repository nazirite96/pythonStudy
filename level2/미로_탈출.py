import collections


def solution(maps):
    def bfs(start_x, start_y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[False for _ in map] for map in maps]
        distance = [[0 for _ in map] for map in maps]

        deque = collections.deque([(start_x, start_y)])
        visited[start_y][start_x] = True

        while deque:
            x, y = deque.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    deque.append((nx, ny))

        return distance

    s_x = s_y = l_x = l_y = e_x = e_y = 0

    for y, map in enumerate(maps):
        if 'S' in map:
            s_y, s_x = y, map.index('S')
        if 'L' in map:
            l_y, l_x = y, map.index('L')
        if 'E' in map:
            e_y, e_x = y, map.index('E')

    distance_to_l = bfs(s_x, s_y)[l_y][l_x]
    distance_to_e = bfs(s_x, s_y)[e_y][e_x]
    distance_from_l_to_e = bfs(l_x, l_y)[e_y][e_x]

    if distance_to_l == 0 or distance_to_e == 0 or distance_from_l_to_e == 0:
        return -1

    return distance_to_l + distance_from_l_to_e

maps = ["SOOOL",
        "XXXXO",
        "OOOOO",
        "OXXXX",
        "OOOOE"]
print(solution(maps))

maps = ["LOOXS",
        "OOOOX",
        "OOOOO",
        "OOOOO",
        "EOOOO"]
print(solution(maps))