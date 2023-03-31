def solution(name, yearning, photo):
    answer = []
    name_yearning = dict(zip(name,yearning))

    for picture in photo:
        sum = 0
        for person in picture:
            if person in name:
                sum += name_yearning[person]
        answer.append(sum)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]

print(solution(name,yearning,[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))