import itertools

def solution(word):
    aeiou = ['A','E','I','O','U']
    list_aeiou = []
    for case in range(1,6):
        list_aeiou.extend(list(map("".join, itertools.product(aeiou, repeat=case))))
    list_aeiou.sort()
    return list_aeiou.index(word) + 1

print(solution('I'))


#
# from itertools import product
# def solution(word):
#     total_dict = []
#     for i in range(1, 6):
#         dictionary = list(map("".join, product(['A','E','I','O','U'], repeat = i)))
#         total_dict.extend(dictionary)
#     total_dict.sort()
#     return total_dict.index(word)+1
#
#
# print(solution('I'))