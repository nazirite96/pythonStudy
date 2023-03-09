def solution(id_list, report, k):
    answer = []
    id_count_dict = {}
    id_reporter_dict = {}
    id_email_count = {}
    for id in id_list:
        id_count_dict[id] = 0
        id_email_count[id] = 0
        id_reporter_dict[id] = []
    # id : count
    for report_str in report:
        reporter, reported_id = report_str.split(' ')
        if reporter not in id_reporter_dict[reported_id]:
            id_reporter_dict.get(reported_id).append(reporter)
            id_count_dict[reported_id] += 1

    for id in id_list:
        if id_count_dict[id] >= k:
            for reporter in id_reporter_dict[id]:
                id_email_count[reporter]+=1

    for id in id_list:
        answer.append(id_email_count[id])

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(id_list, report, 2))