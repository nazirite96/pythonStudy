def solution(spell, dic):
    answer = 2
    for word in dic:
        check_word = True
        for chac in spell:
            if chac not in word:
                check_word = False
                break
        if check_word:
            return 1
    return answer


print(not set([1,2,3]) - set([1,2,3]))
print(not 1)