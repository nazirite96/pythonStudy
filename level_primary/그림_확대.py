def solution(picture, k):
    answer = []
    for line in picture:
        expanded_line = ''
        for pixel in line:
            expanded_line += pixel * k
        for _ in range(k):
            answer.append(expanded_line)

    return answer

picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]

k = 2

print(solution(picture, k))


["..xxxx......xxxx..",
 "..xxxx......xxxx..",
 "xx....xx..xx....xx",
 "xx....xx..xx....xx",
 "xx......xx......xx",
 "xx......xx......xx",
 "..xx..........xx..",
 "..xx..........xx..",
 "....xx......xx....",
 "....xx......xx....",
 "......xx..xx......",
 "......xx..xx......",
 "........xx........",
 "........xx........"]