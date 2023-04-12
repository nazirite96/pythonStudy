import collections
import sys
sys.setrecursionlimit(10000)


def solution(x, y, n):
    # 빈 v array 생성
    v = [0] * 1000001
    # 초기값 설정
    v[x] = 1
    q = collections.deque()
    q.append(x)

    while q:
        cur = q.popleft()
        # 목적지와 같다면 리턴
        if cur == y:
            return v[y] - 1
        for num in (cur+n, cur*2, cur*3):
            if 0 <= num <= 1000000 and v[num] == 0:
                q.append(num)
                # 액션 카운트 +1
                v[num] = v[cur] + 1

    return -1

print(solution(10, 140, 5))
