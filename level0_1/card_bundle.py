def solution(cards1, cards2, goal):

    card1 = cards1.pop(0)
    card2 = cards2.pop(0)
    yes_or_no = True
    for goal_word in goal:
        if card1 == goal_word or card2 == goal_word:
            if card1 == goal_word:
                if len(cards1) != 0:
                    card1 = cards1.pop(0)
                else:
                    card1 = ''
            else:
                if len(cards2) != 0:
                    card2 = cards2.pop(0)
                else:
                    card2 = ''
        else:
            yes_or_no = False

    if yes_or_no:
        return 'Yes'
    else:
        return 'No'
