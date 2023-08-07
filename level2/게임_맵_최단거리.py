from collections import deque

def solution(maps):
       n = len(maps)
       m = len(maps[0])
       visited = [[False]*m for _ in range(n)]
       q = deque()
       q.append((0, 0))
       dx = [-1, 1, 0, 0]
       dy = [0, 0, -1, 1]
       visited[0][0]=True
       while q:
              y, x = q.popleft()
              for i in range(4):
                     nx=x+dx[i]
                     ny=y+dy[i]
                     if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                            if not visited[ny][nx]:
                                   visited[ny][nx] = True
                                   q.append((ny, nx))
                                   maps[ny][nx] = maps[y][x]+1
                                   for map in maps:
                                          print(map)
                                   print('--------------')
       if maps[n-1][m-1]==1:
              return -1
       else:
              return maps[n-1][m-1]




# import copy
#
# def solution(maps):
#     answer = 0
#     m,n = len(maps),len(maps[0])
#     # n = 가로
#     # m = 세로
#     x,y = 0, 0
#     case_len_list = []
#     go_to_nm(x, y, case_len_list, maps, 0, m, n,'S')
#     print(case_len_list)
#     if max(case_len_list) == -1:
#         return -1
#     else:
#         case_len_list.sort()
#         for loads_len in case_len_list:
#             if loads_len != -1:
#                 answer = loads_len
#                 break
#
#     return answer
#
# def go_to_nm(x, y, case_len_list,maps, len, m, n,direction):
#     direction_dict = {'L': [-1, 0], 'R': [1,0], 'U': [0, -1], 'D': [0, 1]}
#     if direction == 'S':
#         maps[y][x] = 2
#         len += 1
#     else:
#         while 0 <= y+direction_dict[direction][1] < m and 0 <= x+direction_dict[direction][0] < n \
#             and maps[y+direction_dict[direction][1]][x+direction_dict[direction][0]] == 1:
#             maps[y][x] = 2
#             y += direction_dict[direction][1]
#             x += direction_dict[direction][0]
#             len += 1
#
#
#     if x == n-1 and y == m-1:
#         case_len_list.append(len)
#         return
#     else:
#         can_not_go = True
#         if x - 1 >= 0 and maps[y][x-1] == 1:
#             go_to_nm(x, y, case_len_list, copy.deepcopy(maps), len, m, n,'L')
#             can_not_go = False
#         if x + 1 < n and maps[y][x + 1] == 1:
#             go_to_nm(x, y, case_len_list, copy.deepcopy(maps), len, m, n,'R')
#             can_not_go = False
#         if y - 1 >= 0 and maps[y-1][x] == 1:
#             go_to_nm(x, y, case_len_list, copy.deepcopy(maps), len, m, n, 'U')
#             can_not_go = False
#         if y + 1 < m and maps[y+1][x] == 1:
#             go_to_nm(x, y, case_len_list, copy.deepcopy(maps), len, m, n, 'D')
#             can_not_go = False
#
#         if can_not_go:
#             case_len_list.append(-1)

print(solution([[1,0,1,1,1],
       [1,0,1,0,1],
       [1,0,1,1,1],
       [1,1,1,0,1],
       [0,0,0,0,1]]))