def solution(picks, minerals):
    answer = 0
    can_earn_minerals = sum(picks) * 5
    minerals = minerals[:can_earn_minerals]
    minerals_nums = []
    for i in range(0,len(minerals),5):
        nums = []
        for mineral in minerals[i:i+5]:
            if mineral == 'diamond':
                nums.append(25)
            elif mineral == 'iron':
                nums.append(5)
            else:
                nums.append(1)
        minerals_nums.append(nums)
    minerals_nums.sort(key= lambda x : sum(x),reverse=True)
    picks_nums = []
    for i,pick in enumerate(picks):
        if i == 0:
            for _ in range(pick):
                picks_nums.append(25)
        elif i == 1:
            for _ in range(pick):
                picks_nums.append(5)
        else:
            for _ in range(pick):
                picks_nums.append(1)

    while minerals_nums and picks_nums:
        minerals_num = minerals_nums.pop(0)
        picks_num = picks_nums.pop(0)
        for mineral_num in minerals_num:
            pirodo = mineral_num // picks_num
            if pirodo == 0:
                answer += 1
            else:
                answer += pirodo
    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))

picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))
