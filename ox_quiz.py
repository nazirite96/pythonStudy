def solution(quizs):
    answer = []

    for quiz in quizs:
        quiz_splited = quiz.split(' ')
        a = int(quiz_splited[0])
        b = int(quiz_splited[2])
        c = int(quiz_splited[4])
        if quiz_splited[1] == '-':
            if a-b == c:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if a+b == c:
                answer.append("O")
            else:
                answer.append("X")

    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))