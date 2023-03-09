from collections import defaultdict


def solution(keymap, targets):
    answer = []
    least_index_key_dick = defaultdict(int)
    for key in keymap:
        for char in key:
            if least_index_key_dick[char] == 0 or least_index_key_dick[char] > key.index(char)+1:
                least_index_key_dick[char] = key.index(char)+1
    for target in targets:
        result = 0
        for char in target:
            if char in least_index_key_dick:
                result += least_index_key_dick[char]
            else:
                result = -1
                break
        answer.append(result)
    return answer

keymap = ["O","IO"]
targets = ["O"]
print(solution(keymap, targets))