def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    n = len(citations)
    for i in range(0,n+1):
        count = 0
        for j,citation in enumerate(citations):
            if citation >= i:
                count = n-j
                break
        if i <= count:
            answer = i
    return answer




print(solution([1,3,9,7,2,8,5,6,4,0]))
print(solution([1]))
print(solution([100000]))
print(solution([0,1,2,3,4]))
print(solution([0,1,6,4,6,6,6,6,10,10,10,10,9,8,10,10,10,10,9,8,10,10,10,10,9,8]))
print(solution([9999,5000,1000,2000,1000]))