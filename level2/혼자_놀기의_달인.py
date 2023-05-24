def solution(cards):
    is_first = True
    opened = [False] * len(cards)
    cards = [i - 1 for i in cards]
    case_card = [case_choose(cards, i, is_first, opened.copy()) for i in range(len(cards))]
    return max(case_card)

def case_choose(cards, n, is_first, opened):
    count = 0
    a = n
    while not opened[a]:
        count += 1
        opened[a] = True
        a = cards[a]
    if is_first:
        case_card = [case_choose(cards, i, False, opened.copy()) for i in range(len(cards)) if not opened[i]]
        if case_card:
            return count * max(case_card)
        else:
            return 0
    else:
        return count



cards = [2,3,1,5,4]
print(solution(cards))

cards = [3,1,2,5,6,4]
print(solution(cards))
cards = [6,2,3,4,5,1]
cards = [1,2,3,4,5,6]
cards = [1,2]
print(solution(cards))
