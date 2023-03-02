def solution(A, B):
    answer = -1
    count = 0
    for i in range(len(A)):
        if A == B:
            answer = count
            break;
        B = B[1:len(B)] + B[0]
        count += 1
        print(B)
        print(count)
    return answer

print(solution('hello', 'ohell'))