def solution(arr, delete_list):
    answer = [x for x in arr if x not in delete_list]
    return answer

print(solution([293, 1000, 395, 678, 94],[94, 777, 104, 1000, 1, 12]))