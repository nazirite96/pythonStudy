def solution(todo_list, finished):
    return [todo for i,todo in enumerate(todo_list) if not finished[i]]

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))