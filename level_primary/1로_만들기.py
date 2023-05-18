def solution(num_list):
    answer = 0
    for num in num_list:
        a = num
        while a != 1:
            if a % 2 == 0:
                a /= 2
            else:
                a -= 1
                a /= 2
            answer += 1
    return answer

num_list = [12, 4, 15, 1, 14]

print(solution(num_list))