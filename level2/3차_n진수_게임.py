def solution(n, t, m, p):
    answer = '0'

    list_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    list_str = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    mapper_dict = dict(zip(list_num,list_str))
    count = 1
    while len(answer[p - 1::m][0:t]) < t:
        num = count
        rev_base = ''
        while num > 0:
            num, mod = divmod(num ,n)
            rev_base += mapper_dict.get(mod)
        rev_base = rev_base[::-1]
        answer += rev_base
        count += 1

    return answer[p-1::m][0:t]

# print(solution(2,4,2,1))
print(solution(16,16,2,1))
# print(solution(16,16,2,2))