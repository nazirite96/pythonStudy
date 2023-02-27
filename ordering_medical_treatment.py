def solution(emergency):
    answer = []
    emergency_org = emergency.copy()
    emergency.sort(reverse=True)
    dictionary = {emergency[i] : i+1 for i in range(len(emergency))}
    for i in emergency_org:
        answer.append(dictionary.get(i))
    return answer

emergency = [3, 76, 24]
print(solution(emergency))