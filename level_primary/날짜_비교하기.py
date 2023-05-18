def solution(date1, date2):
    days_one = 365 * date1[0] + 31 * date1[1] + date1[2]
    days_two = 365 * date2[0] + 31 * date2[1] + date2[2]
    return int(days_one < days_two)

date1 = [2021, 12, 28]
date2 = [2021, 12, 29]

print(solution(date1, date2))

date1 = [1024, 10, 24]
date2 = [1024, 10, 24]

print(solution(date1, date2))