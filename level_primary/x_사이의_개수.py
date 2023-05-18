def solution(my_string):
    return [len(x) for x in my_string.split('x')]

my_str = 'oxooxoxxox'
print(solution(my_str))