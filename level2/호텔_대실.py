def solution(book_time):
    book_time = sorted(book_time, key=lambda time: time[0])
    room = []
    book_time_minute = []
    for start,end in book_time:
        start_splited = start.split(':')
        end_splited = end.split(':')
        book_time_minute.append((int(start_splited[0]) * 60 + int(start_splited[1]),(int(end_splited[0]) * 60 + int(end_splited[1]) + 10)))
    max_room_count = 0
    for now in range(24 * 60):
        # print(now//60 ,now % 60)
        count = 0
        for start,end in book_time_minute:
            if start <= now < end:
                count += 1
        if count > max_room_count:
            max_room_count = count

    return max_room_count

book_time = [["00:00","23:58"],["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time = [["00:01","00:10"],["00:19","00:29"],["00:19","00:20"],["00:20","00:29"]]

print(solution(book_time))


book_time = [["09:10", "10:19"], ["10:20", "12:20"], ["12:19","12:30"]]

print(solution(book_time))

book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]

print(solution(book_time))
