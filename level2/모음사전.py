import itertools


def solution(word):
    answer = 0
    aeiou = ['A','E','I','O','U']
    list_aeiou = []
    for case in range(1,6):
        for i in list(itertools.combinations_with_replacement(aeiou,case)):
            list_aeiou.append(''.join(i))
    list_aeiou.sort()
    print(list_aeiou)

    return list_aeiou.index(word)+1

print(solution('EIO'))