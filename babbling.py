import itertools


def solution(babbling):
    answer = 0
    count = 0
    babbling_can_use = ["aya", "ye", "woo", "ma"]
    babbling_all = []
    np2 = itertools.permutations(babbling_can_use, 2);
    np3 = itertools.permutations(babbling_can_use, 3);
    np4 = itertools.permutations(babbling_can_use, 4);
    for babb in babbling_can_use:
        babbling_all.append(babb)

    for babb in np2:
        text = ''
        for np in babb:
            text += np
        babbling_all.append(text)

    for babb in np3:
        text = ''
        for np in babb:
            text += np
        babbling_all.append(text)

    for babb in np4:
        text = ''
        for np in babb:
            text += np
        babbling_all.append(text)

    for babb in babbling:
        if babb in babbling_all:
            answer += 1

    return answer


babbling_list = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling_list))


babbling_can = ["aya", "ye", "woo", "ma"]



