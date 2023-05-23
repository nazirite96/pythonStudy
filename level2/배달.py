can_delivery = []
import sys
sys.setrecursionlimit(10**6)

def bfs(current_town, K, count, road_connect_info,road_hour_info, is_visited):
    global can_delivery

    if K >= count and not is_visited[current_town] :
        is_visited[current_town] = True
        can_delivery[current_town] = True
        for target_town in road_connect_info[current_town]:
            used_hour = count + road_hour_info[(current_town,target_town)]
            bfs(target_town, K, used_hour, road_connect_info, road_hour_info, is_visited.copy())

def solution(N, road, K):
    answer = 0
    global can_delivery


    can_delivery = [False for _ in range(N+1) ]
    road_connect_info = [[] for _ in range(N+1)]
    road_hour_info = {}
    is_visited = [False for _ in range(N+1)]

    for a, b, c in road:
        if b not in road_connect_info[a]:
            road_connect_info[a].append(b)
            road_connect_info[b].append(a)
        if (a, b) not in road_hour_info:
            road_hour_info[(a, b)] = c
            road_hour_info[(b, a)] = c
        else:
            if road_hour_info[(a, b)] > c:
                road_hour_info[(b, a)] = c
                road_hour_info[(a, b)] = c
    distances = {node: float('infinity') for node in road_connect_info}
    print(distances)
    bfs(1, K, 0, road_connect_info,road_hour_info,is_visited)
    answer = can_delivery.count(True)

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))



N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

print(solution(N, road, K))

N = 4
road = [[1,2,2],[1,3,2],[1,4,4],[2,3,4],[2,4,2],[3,4,2]]
K = 3

print(solution(N, road, K))