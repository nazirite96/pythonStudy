def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for index,peo in enumerate(people):

        if peo == 241:
            break
        space = limit - peo
        rever_index = len(people)-1
        print(people)
        while people[rever_index] <= space and rever_index > index:
            space -= people[rever_index]
            people.pop(rever_index)
            print(space)
            rever_index -= 1

    return len(people)

print(solution([30,30,40,20],100))