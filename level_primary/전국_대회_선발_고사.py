def solution(rank, attendance):
    answer = 0
    removed_rank = []
    for i,k in enumerate(rank):
        if attendance[i]:
            removed_rank.append(k)

    sorted_rank = sorted(removed_rank)
    print(sorted_rank)
    answer = rank.index(sorted_rank[0]) * 10000 + rank.index(sorted_rank[1]) * 100 + rank.index(sorted_rank[2])
    return answer

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))


