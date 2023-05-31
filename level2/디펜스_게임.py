import heapq

def solution(n, k, enemy):
    answer = 0
    heapq_list = []
    for i, e in enumerate(enemy):
        n -= e
        heapq.heappush(heapq_list,-e)
        if n >= 0:
            answer += 1
        else:
            while k > 0 > n:
                used_k = heapq.heappop(heapq_list)
                n -= used_k
                k -= 1
            if n >= 0:
                answer += 1
            else:
                break
    return answer

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

print(solution(n, k, enemy))

n = 2
k = 4
enemy = [3, 3, 3, 3]
print(solution(n, k, enemy))