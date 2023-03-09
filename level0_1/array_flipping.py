def solution(num_list):
    answer = []
    for i in num_list:
        answer.insert(0,i)

    return answer


print(solution([1,2,3,4,5]))
