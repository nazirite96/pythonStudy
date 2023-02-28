def solution(dots):
    ab = slopee(dots[0],dots[1])
    ac = slopee(dots[0],dots[2])
    ad = slopee(dots[0],dots[3])
    bc = slopee(dots[1],dots[2])
    bd = slopee(dots[1],dots[3])
    cd = slopee(dots[2],dots[3])
    s1 = set([ab, cd])
    s2 = set([ac, bd])
    s3 = set([ad, bc])
    return len(s1) != 2 or len(s2) != 2 or len(s3) != 2

def slopee(dot1,dot2):
    x = (dot1[1] -dot2[1]) / (dot2[0] - dot1[0])
    return x

print(solution([[1, 1], [2, 2], [3, 3], [4, 4]]))
