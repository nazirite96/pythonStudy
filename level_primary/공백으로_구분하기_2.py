def solution(my_string):
    return [x for x in my_string.split(' ') if len(x) != 0]