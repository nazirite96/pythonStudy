from collections import defaultdict

def solution(lines):
    answer = 0
    #dict에 숫자 추가
    overlap_check_dict = defaultdict(int)
    for line in lines:
        for i in range(line[0],line[1]):
            overlap_check_dict[i] += 1
    keys = overlap_check_dict.keys()
    for key in keys:
        if overlap_check_dict.get(key) > 1:
            answer += 1
    return answer

print(solution([[0, 5], [3, 9], [1, 10]]))
