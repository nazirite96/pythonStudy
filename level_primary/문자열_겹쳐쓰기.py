def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

my_string = 'He11oWor1d'
overwrite_string = 'lloWorl'
print(solution(my_string, overwrite_string, 2))

my_string = 'Program29b8UYP'
overwrite_string = 'merS123'
print(solution(my_string, overwrite_string, 7))
