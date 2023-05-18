def solution(myString, pat):
    return myString[:myString.rindex(pat) + len(pat)]

myString = 'AbCdEFG'
pat = 'dE'
print(solution(myString, pat))
myString = 'AAAAaaaa'
pat = 'a'
print(solution(myString, pat))
