def solution(relations):
    answer = []
    targets = [[i for i in range(len(relations[0]))]]
    while targets:
        check = 0
        tmp = targets.pop(0)
        for i in range(len(tmp)):
            lst = []
            for leng in range(len(relations)):
                a = tmp.copy()
                a.remove(tmp[i])
                b = ''
                for x in a:
                    b += relations[leng][x]
                lst.append(b)
            if (len(set(lst)) == len(lst)) and (a not in targets):
                targets.append(a)
            elif (len(set(lst)) != len(lst)):
                check +=1
        if check ==len(tmp):
            answer.append(tmp)
    return len(answer)


relation = [['a','aa'],['aa','a'],['a','aa']]
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))
