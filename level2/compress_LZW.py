def solution(msg):
    answer = []
    #길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    lzw_dict = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    index = 0
    print(msg[0:3] in lzw_dict)

    while index < len(msg):
        until = 1
        #사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        while True:
            if msg[index:index+until] in lzw_dict and len(msg)!=1:
                until += 1
            else:
                answer.append(lzw_dict.index(msg[index:index+until - 1])+1)
                lzw_dict.append(msg[index:index+until])
                print(answer)
                msg = msg[index+until-1:]
                print(msg)


    return answer


print(solution("O"))