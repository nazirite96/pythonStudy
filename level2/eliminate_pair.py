def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(len(stack) == 0)


print(solution('cdcd'))
print(solution('cddccc'))
