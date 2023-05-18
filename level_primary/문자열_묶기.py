from collections import Counter


def solution(strArr):
    answer = 0
    len_list = [len(str) for str in strArr]
    counter = Counter(len_list)
    return max(counter.values())

strArr = ["a","bc","d","efg","hi"]

print(solution(strArr))