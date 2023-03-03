def solution(M, N):
    return (M)*(N-1)+(M-1)


print(solution(1,1)==0)
print(solution(1,2)==1)
print(solution(1,3)==2)
print(solution(1,4)==3)
print(solution(2,5)==9)
print(solution(2,6)==11)