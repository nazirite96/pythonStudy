def solution(myStr):
    answer = []
    abc = ['a', 'b', 'c']
    for div in abc:
        myStr = myStr.replace(div, '0')
    splited_str = myStr.split('0')
    answer = [str for str in splited_str if len(str) != 0]
    if len(answer) == 0:
        return ['EMPTY']
    return answer

print(solution('baconlettucetomato'))