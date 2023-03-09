def solution(cipher, code):
    list_ciper = []
    for i in range(code-1, len(cipher), code):
        list_ciper.append(cipher[i])
    return ''.join(list_ciper)

print(solution("pfqallllabwaoclk",2))