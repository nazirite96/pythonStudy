def solution(order):
    answer = 0

    for menu in order:
        if 'cafe' in menu:
            answer += 5000
        else:
            answer += 4500
    return answer

order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
print(solution(order))


order = ["americanoice", "americano", "iceamericano"]
print(solution(order))