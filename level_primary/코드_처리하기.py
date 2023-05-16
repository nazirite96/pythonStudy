def solution(code):
    mode = 0
    ret = []
    for i,char in enumerate(code):
        if char == '1':
            mode += 1
            mode %= 2
        else:
            if mode == 0 and i % 2 == 0:
                ret.append(char)
            elif mode == 1 and i % 2 == 1:
                ret.append(char)
    if len(ret) == 0:
        return 'EMPTY'
    return ''.join(ret)


code = "abc1abc1abc"
print(solution(code))