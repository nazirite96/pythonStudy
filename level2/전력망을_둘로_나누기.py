cnt = 0
def DFS(v1, check, graph):
    global cnt
    check[v1] = 1
    cnt += 1
    for i in graph[v1]:
        if check[i] == 0:
            DFS(i, check, graph)


def solution(n, wires):
    global cnt
    answer = 100

    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        check = [0]*(n+1)
        check[v2] = 1
        cnt = 0
        DFS(v1, check, graph)
        answer = min(answer, abs(cnt-(n-cnt)))

    return answer