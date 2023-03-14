def solution(n, words):
    answer = []
    already_used_word = []
    end = words[0][-1]
    for i,word in enumerate(words):

        if word not in already_used_word and word[0] == end or i == 0:
            end = word[-1]
            already_used_word.append(word)
        else:
            answer.append(i % n + 1)
            answer.append(i//n + 1)
            break
    if len(answer) == 0 :
        answer = [0, 0]
    return answer
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))