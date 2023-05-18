def solution(myString, pat):
    change_pat = ''
    for char in pat:
        if char == 'A':
            change_pat += 'B'
        else:
            change_pat += 'A'
    return int(change_pat in myString)

print(solution("ABBAA",	"AABB"))
print(solution("ABAB",	"ABAB"))
