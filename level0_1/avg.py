def solution(numbers):
    answer = 0

    for num in numbers:
        answer += num
    answer = answer / len(numbers)

    return answer


nubmers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(nubmers))