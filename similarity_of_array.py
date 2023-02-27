
def solution(s1, s2):
    answer = 0
    for str1 in s1:
        if s2.count(str1) > 0:
            answer+=1
    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))