import decimal

def solution(price):
    answer = 0
    discount = 1
    if price >= 100000:
        discount = 0.95
    if price >= 300000:
        discount = 0.90
    if price >= 500000:
        discount = 0.80

    answer = int(price * discount)

    return answer

print(solution(1000000))
