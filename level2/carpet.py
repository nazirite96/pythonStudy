def solution(brown, yellow):
    answer = []
    # brown + yellow = 넓이
    for width in range(1,int((yellow+brown) ** 1/2)+1):
        if yellow % width == 0:
            height = yellow // width
            if (height+2) * (width+2) - yellow == brown:
                return [height+2,  width+2]
    return answer