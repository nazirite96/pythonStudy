def solution(num_list, n):
    answer = []
    index = 0
    for i in range(int(len(num_list)/n)):
        n_list = []
        for j in range(n):
            n_list.append(num_list[index])
            index += 1
        answer.append(n_list)

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))