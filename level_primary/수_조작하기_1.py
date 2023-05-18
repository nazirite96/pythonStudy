def solution(n, control):
    answer = 0
    for command in control:
        if command == 'w':
            answer += 1
        elif command == 's':
            answer -= 1
        elif command == 'd':
            answer += 10
        elif command == 'a':
            answer -= 10
    return answer

print(solution(0,'wsdawsdassw'))
