def solution(s, skip, index):
    answer = ''
    s_ord_list = [ord(char) for char in s]
    skip_ord_list = [ord(char) for char in skip]
    print(skip_ord_list)
    end = ord('z')
    start = ord('a')
    for i,s_ord in enumerate(s_ord_list):
        count = 1
        while count <= index:
            s_ord += 1
            count += 1
            if s_ord > end:
                s_ord = start
            while s_ord in skip_ord_list:
                s_ord += 1
                if s_ord > end:
                    s_ord = start
        s_ord_list[i] = s_ord
    s_chr_list = [chr(ord) for ord in s_ord_list]

    return answer.join(s_chr_list)

print(solution('aukks','wbqd',5))