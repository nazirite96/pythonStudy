def solution(sides):
    answer = (max(sides)-(max(sides)-min(sides)) + ((max(sides)+min(sides)-1)-max(sides)))
    #sides의 맥스가 가장 긴변일 경우
    #max - (max-min) +

    return answer