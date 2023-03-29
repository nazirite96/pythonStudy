def solution(files):
    files_head_num_dict = {}
    for file in files:
        file_len = len(file)
        head_end, number_end = 0, 0
        while not file[head_end].isdigit():
            head_end += 1
        number_end = head_end
        while number_end < file_len and file[number_end].isdigit() and number_end - head_end < 5:
            number_end += 1
        files_head_num_dict[file] = [file[0:head_end].lower(), int(file[head_end:number_end])]
    answer = [file[0] for file in sorted(files_head_num_dict.items(), key=lambda head_num: (head_num[1][0],head_num[1][1]))]

    return answer

print(solution(["A-15","F-5 Freedom Fighter","A-0000000000 woongs", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))