def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)

    return result


# def solution(numbers):
#     answer = [-1] * len(numbers)
#     back_max = numbers[-1]
#     for i in range(len(numbers)-2, -1, -1):
#         if numbers[i] >= back_max:
#             back_max = numbers[i]
#             continue
#         for j in range(i+1,len(numbers)):
#             if numbers[j] > numbers[i]:
#                 answer[i] = numbers[j]
#                 break
#             if numbers[j] <= numbers[i] < answer[j]:
#                 answer[i] = answer[j]
#                 break
#     return answer

# def solution(numbers):
#     answer = []
#
#     stack_of_num = []
#     for i in range(len(numbers)):
#         is_not_big = True
#         for j in range(i+1,len(numbers)):
#             if numbers[i] < numbers[j]:
#                 is_not_big = False
#                 answer.append(numbers[j])
#                 break
#         if is_not_big:
#             answer.append(-1)
#     return answer


# print(solution([2, 3, 3, 5]))
# print(solution([1, 2, 3, 4]))
print(solution([9, 1, 5, 3, 6, 2]))

