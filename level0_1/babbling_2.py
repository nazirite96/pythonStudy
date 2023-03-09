def solution(babbling):
    answer = 0

    can_badd_list = [ "aya", "ye", "woo", "ma"]
    for do_badd in babbling:
        for can_badd in can_badd_list:
            if can_badd in do_badd:
                do_badd = do_badd.replace(can_badd,'#')
                if '##' in do_badd:
                    break
                else:
                    do_badd = do_badd.replace('#', '*')
        set_do_badd = set(do_badd)
        if len(set_do_badd) == 1 and set_do_badd.pop() == '*':
            answer += 1

    return answer

print(solution(["aya", "yee", "yeye", "maa","ayayeaya"]))