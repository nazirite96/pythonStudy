def solution(n):
    answer = []
    # 현재 위치 , 중간, 가야할 위치, depth , 현재 n, answer
    hanois_top(1,2,3,n,answer)
    return answer

def hanois_top(current_location, not_target, target,n,answer):
    if n == 1:
        answer.append([current_location,target])
    else:
        hanois_top(current_location,target,not_target,n-1,answer)
        answer.append([current_location,target])
        hanois_top(not_target,current_location,target,n-1,answer)

print(solution(3))