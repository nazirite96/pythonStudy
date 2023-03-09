def solution(today, terms, privacies):
    answer = []
    today_converted = convert_days_at_zero(today)
    dict_terms = {y.split()[0]: int(y.split()[1]) * 28 for y in terms}
    for i, privacy in enumerate(privacies):
        if today_converted >= (convert_days_at_zero(privacy.split()[0]) +
                               dict_terms[privacy.split()[1]]):
            answer.append(i + 1)
    return answer


def convert_days_at_zero(day):
    today = [int(x) for x in day.split('.')]
    years = today[0] * 12 * 28
    months = today[1] * 28
    day = today[2]
    return years + months + day


print(solution("2022.05.19",
               ["A 6", "B 12", "C 3"],
               ["2021.05.02 A", "2021.07.01 B",
                "2022.02.19 C", "2022.02.20 C"]))
