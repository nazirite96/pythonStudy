def solution(n):
    answer = n
    one_count = bin(n).count('1')              # N의 2의진수의 1의 갯수
    while True:
        answer += 1
        answer_count = bin(answer).count('1')
        if answer_count == one_count:
            break
    return answer


print(solution(78)==83)
print(solution(15)==23)
print(solution(9)==10) # 1001 1010
print(solution(100)==104) # 1100100 1101000
print(solution(1)==2) # 1 10
print(solution(6)==9) # 110 1001
print(solution(5)==6) # 101 110
print(solution(7)==11) # 111 1011
print(solution(8)==16) # 1000 10000
print(solution(9)==10) # 1001 1010
print(solution(10)==12) # 1010 1100
print(solution(11)==13) # 1011 1101
print(solution(12)==17) # 1100 10001
print(solution(13)==14) # 1101 1110
print(solution(14)==19) # 1110 10011
print(solution(15)==23) # 1111 10111
print(solution(16)==32) # 10000 100000


