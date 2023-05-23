from collections import defaultdict
import heapq

def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distances = {node: float('infinity') for node in graph}

    distances[1] = 0

    # 시작 지점의 거리
    queue = [(0, 1)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        # 이미 거리가 넘어간 case는 패스
        if distances[current_node] < current_distance:
            continue

        for target, target_distance in graph[current_node]:
            # 중첩된 거리 + 타겟까지의 거리를 구한다.
            distance = current_distance + target_distance
            # 만약에 이미 타겟까지 거리가 더 짧은 것이 존재한다면
            if distance < distances[target]:
                # 최단 동선으로 움직인 이 case에서 다른 노드를 가는 거리를 계산한다.
                distances[target] = distance
                heapq.heappush(queue, (distance, target))

    answer = len([d for d in distances.values() if d <= K])

    return answer


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4
# print(solution(N, road, K))
#
# N = 4
# road = [[1,2,2],[1,3,2],[1,4,4],[2,3,4],[2,4,2],[3,4,2]]
# K = 3
# print(solution(N, road, K))