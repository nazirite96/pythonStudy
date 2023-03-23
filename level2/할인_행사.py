from collections import Counter
def solution(want, number, discount):
    answer = 0
    wants_numbers = dict(zip(want, number))
    print(wants_numbers)
    for i in range(len(discount)-9):
        is_it_vaild = True
        sales_item = Counter(discount[i:i+10])
        for wanted_item in want:
            if wanted_item not in sales_item or wants_numbers[wanted_item] > sales_item[wanted_item]:
                is_it_vaild = False
                break
        if is_it_vaild : answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))