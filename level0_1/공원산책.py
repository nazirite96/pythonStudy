def solution(park, routes):
    comand = {'E': [1, 0], 'W': [-1, 0], 'S': [0, 1], 'N': [0, -1]}
    width = len(park[0])
    height = len(park)
    x, y = 0, 0
    for i, load in enumerate(park):
        if 'S' in load:
            x = load.index('S')
            y = i
    for route in routes:
        direction, distance = route.split(' ')
        can_go = True
        save_x = x
        save_y = y
        for next_route in range(int(distance)):
            if (save_x + comand[direction][0]) == width \
                    or (save_x + comand[direction][0]) < 0 \
                    or (save_y + comand[direction][1]) < 0 \
                    or (save_y + comand[direction][1]) == height \
                    or park[save_y + comand[direction][1]][save_x + comand[direction][0]] == 'X':
                can_go = False
                print(direction,save_y,save_x)
                break
            save_x += comand[direction][0]
            save_y += comand[direction][1]

        if can_go:
            x += (comand[direction][0] * int(distance))
            y += (comand[direction][1] * int(distance))

    return [y, x]


print(solution(["SOO","OXX","OOO"], ["E 2","S 3","W 1"]))
