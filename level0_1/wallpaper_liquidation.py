def solution(wallpaper):
    lux = 51
    luy = 51
    rdx = 0
    rdy = 0

    len_of_line = len(wallpaper[0])

    for y,line in enumerate(wallpaper):
        reversed_line = line[::-1]
        if '#' in line:
            if y < lux :
                lux = y
            if luy > line.index('#'):
                luy = line.index('#')
            if len_of_line - reversed_line.index('#') > rdy:
                rdy = len_of_line - reversed_line.index('#')
            if rdx < y + 1:
                rdx = y + 1


    answer = [lux, luy, rdx, rdy]
    return answer

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]

print(solution(wallpaper))