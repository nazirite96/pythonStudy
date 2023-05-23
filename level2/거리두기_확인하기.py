def solution(places):
    answer = []
    for place in places:
        answer.append(int(check_distance(place)))
    return answer


def check_distance(place):
    place = [list(line) for line in place]
    for i in range(5):
        for j in range(5):
            if i < 3:
                if (place[j][i] == 'P' and place[j][i+1] == 'P') or \
                        (place[j][i+1] == 'P' and place[j][i+2] == 'P') or \
                        (place[j][i] == 'P' and place[j][i+1] == 'O' and place[j][i+2] == 'P'):
                    return False
            if j < 3:
                if (place[j][i] == 'P' and place[j+1][i] == 'P') or \
                        (place[j+1][i] == 'P' and place[j+2][i] == 'P') or \
                        (place[j][i] == 'P' and place[j+1][i] == 'O' and place[j+2][i] == 'P'):
                    return False
            if i < 4 and j < 4:
                if (place[j][i] == place[j+1][i+1] == 'P' and (place[j+1][i] == 'O' or place[j][i+1] == 'O')) or \
                        (place[j+1][i] == place[j][i+1] == 'P' and (place[j][i] == 'O' or place[j+1][i+1] == 'O')):
                    return False
    return True


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX",
           "OXPXP",
           "OXXXO",
           "OXXXO",
           "OOOXP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))