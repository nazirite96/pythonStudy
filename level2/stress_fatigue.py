import itertools

def solution(k, dungeons):
    answer = -1
    dungeons_len = len(dungeons)

    dungeons_number = [i for i in range(dungeons_len)]
    case_dungeons = list(itertools.permutations(dungeons_number, dungeons_len))
    for case in case_dungeons:
        pirodo = k
        adventured_dungeons = 0
        for visit_dungeons_num in case:
            if pirodo >= dungeons[visit_dungeons_num][0]:
                pirodo -= dungeons[visit_dungeons_num][1]
                adventured_dungeons += 1
        if adventured_dungeons > answer:
            answer = adventured_dungeons

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))