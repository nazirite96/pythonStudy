def solution(s):
    answer = []
    s_list = s[1:-1].replace('},','*').replace('{','').replace('}','').split('*').sort(key=len)
    for s_str in s_list:
        for s_num in [int(s_num_str) for s_num_str in s_str.split(',')]:
            if s_num not in answer:
                answer.append(s_num)
    return answer
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))