def solution(elements):
    elements_double = elements * 2
    sum_set = set()
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            sum_set.add(sum(elements_double[j:j+i]))
    return len(sum_set)

print(solution([7,9,1,1,4]))