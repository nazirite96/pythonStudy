from datetime import datetime


def solution(m, musicinfos):
    answer_list = []
    notes_shop = { 'C#': '2','D#': '4', 'F#' : '7', 'G#': '9', 'A#': '@'}
    notes = {'C': '1','D': '3', 'E': '5','F': '6', 'G': '8', 'A': '!', 'B': '#'}
    titles = []

    title_playtime = {}
    title_melody = {}
    for note in notes_shop.keys():
        if note in m:
            m = m.replace(note,notes_shop[note])
    for note in notes.keys():
        if note in m:
            m = m.replace(note,notes[note])

    for music in musicinfos:
        splited_info = music.split(',')
        title = splited_info[2]
        titles.append(title)
        d1 = datetime.strptime(splited_info[0], '%H:%M')
        d2 = datetime.strptime(splited_info[1], '%H:%M')
        playtime = (d2 - d1).seconds // 60
        title_playtime[title] = playtime
        for note in notes_shop.keys():
            if note in splited_info[3]:
                splited_info[3] = splited_info[3].replace(note, notes_shop[note])
        for note in notes.keys():
            if note in splited_info[3]:
                splited_info[3] = splited_info[3].replace(note, notes[note])
        melody = ''
        song_length = len(splited_info[3])
        for i in range(playtime):
            melody += splited_info[3][i % song_length]
        title_melody[title] = melody
    for melody in title_melody.values():
        if m in melody:
            for title in title_melody.keys():
                if title_melody[title] == melody:
                    answer_list.append(title)
    if len(answer_list) == 0:
        return '(None)'
    if len(answer_list) == 1:
        return answer_list[0]
    else:
        playtimes = list(title_playtime.values())
        playtimes.sort(reverse=True)
        if playtimes[0] != playtimes[1]:
            for title in title_playtime.keys():
                if title_playtime[title] == playtimes[0]:
                    return title
        else:
            answer_list = []
            for title in title_playtime.keys():
                if title_playtime[title] == playtimes[0]:
                    answer_list.append(title)
            for title in titles:
                if title in answer_list:
                    return title

    return '(None)'

# m = "CDEFGAC"
# musicinfos =  ["12:00,12:06,HELLO,CDEFGA"]
# print(solution(m, musicinfos))
# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#
# print(solution(m, musicinfos))
#
# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
#
# print(solution(m, musicinfos))
#
m = "ABC"
musicinfos = ["00:00,00:02,HEL3LO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF", "13:00,13:05,TEST,ABCDEG#"]

print(solution(m, musicinfos))
#
#
# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,ABCEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#
# print(solution(m, musicinfos))
#
# m = "ABC"
# musicinfos = ["14:00,14:05,TEST,ABCEFG", "13:00,13:05,HELLO,ABCDEF","15:00,15:05,WORLD,ABCDER"]
#
# print(solution(m, musicinfos))
#
# m = "FABA"
# musicinfos = ["14:00,14:05,TEST,ABCEFG", "13:00,13:05,HELLO,ABCDEF","15:00,15:05,WORLD,ABCDER"]
#
# print(solution(m, musicinfos))

