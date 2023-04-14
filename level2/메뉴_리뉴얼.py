import itertools
from collections import Counter


def solution(orders, course):
    answer = []

    for case in course:
        filted_orders = []
        for order in orders:
            if len(order) >= case:
                filted_orders.append(order)
        all_orders = ''.join(filted_orders)
        counter = Counter(all_orders)
        alpa = []
        for count in counter:
            if counter[count] != 1:
                alpa.append(count)
        count_case = {i: [] for i in range(len(orders)+1)}
        combinations = list(itertools.combinations(alpa, case))
        max_count = 2
        for combination in combinations:
            count = 0
            for order in orders:

                if len(order) >= case:
                    case_in_order = True
                    for element in combination:
                        if element not in order:
                            case_in_order = False
                            break
                    if case_in_order: count += 1
            if max_count <= count:
                count_case[count].append(combination)
                max_count = count
        for i in range(len(orders), 1,-1):
            if len(count_case[i]) != 0:
                for correted in count_case[i]:
                    answer.append(''.join(sorted(correted)))
                break
    answer.sort()
    return answer



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

print(solution(orders, course))