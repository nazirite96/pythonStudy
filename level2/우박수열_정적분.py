
def solution(k, ranges):
    answer = []
    collatz_list = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
            collatz_list.append(k)
        else:
            k = k * 3 + 1
            collatz_list.append(k)
    area_list = []
    for i in range(1, len(collatz_list)):
        down = min(collatz_list[i-1],collatz_list[i])
        up = max(collatz_list[i-1],collatz_list[i])
        area_list.append((up - down) / 2 + down)
    print(area_list)
    for a,b in ranges:
        if a > len(area_list)+b:
            answer.append(-1.0)
        else:
            answer.append(sum(area_list[a:len(area_list)+b]))
    return answer


k = 5
ranges = [[0,0],[0,-1],[2,0],[3,-3]]
print(solution(k, ranges))

