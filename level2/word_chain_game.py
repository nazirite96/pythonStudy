def solution(n, words):
    answer = []

    remove_duplicated = set(words)
    if len(remove_duplicated) == len(words):
        return [0,0]
    else:
        removed_word = [word for word in words if word not in remove_duplicated]
        print(removed_word)


    return answer
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))