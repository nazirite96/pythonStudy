def solution(arr):
    gcd = 0
    lcm = arr[0]
    for i in range(1,len(arr)):
        for k in range(1,arr[i]+1):
            if lcm % k == 0 and arr[i] % k == 0:
                gcd = k
        lcm = lcm * arr[i] // gcd
    return lcm

print(solution([1,2,3,4]))