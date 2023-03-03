# def solution(score):
#     a = sorted(list(set([(x[0] + x[1]) for x in score])),reverse=True)
#     answer = [a.index(x[0] + x[1]) + 1 for x in score]
#     before_answer = answer.copy()
#     counted_rank = []
#     count = 0
#     for at in answer:
#         if answer.count(at)-1 != 0 and at not in counted_rank:
#             count += answer.count(at)-1
#             counted_rank.append(at)
#
#     first_t = True
#     for t in range(max(before_answer),0,-1):
#         if answer.count(t) != 1 and first_t:
#             count = count - (before_answer.count(t)-1)
#         first_t = False
#         for k,v in enumerate(answer):
#             if t == v:
#                 answer[k] = v + count
#         print(before_answer.count(t-1))
#         if before_answer.count(t-1) > 1:
#             count = count - (before_answer.count(t-1)-1)
#     return answer

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]


print(solution(	[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))