def solution(food):
    answer = ''
    food_list_a = []
    food_list_b = []
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            food_list_a.append(str(i))
            food_list_b.insert(0,str(i))
    print(food_list_a)
    print(food_list_b)
    a = ''.join(food_list_a)
    b = ''.join(food_list_b)

    return a+'0'+b


print(solution([1, 2, 3, 4, 5, 6,7]))