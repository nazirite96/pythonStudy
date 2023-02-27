def solution(dots):
    ab = slopee(dots[0],dots[1])
    ac = slopee(dots[0],dots[2])
    ad = slopee(dots[0],dots[3])
    bc = slopee(dots[1],dots[2])
    bd = slopee(dots[1],dots[3])
    cd = slopee(dots[2],dots[3])
    s = set([ab, ac, ad, bc, bd, cd])
    return len(s) != 6

def slopee(dot1,dot2):
    x = (dot1[1] -dot2[1]) / (dot2[0] - dot1[0])
    return x

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
