import collections
import itertools


def solution(relation):
    table = collections.defaultdict(list)
    for row in relation:
        for column,value in enumerate(row):
            table[column].append(value)
    keys_lenth = len(relation[0])
    keys = table.keys()
    hubo_keys = []
    for kl in range(keys_lenth):
        combinations_s = itertools.combinations(keys, kl)
        for i in combinations_s:
            now_key = ''.join([str(s_) for s_ in i])
            check = False
            for hubo_key in hubo_keys:
                if hubo_key in now_key:
                    check = True
                    break
            if check:
                continue
            s = set()
            for row in relation:
                make_key = ''
                for i_ in i:
                    make_key += row[i_]
                s.add(make_key)
            if len(s) == len(relation):
                hubo_keys.append(''.join([str(s_) for s_ in i]))

    return len(hubo_keys)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))