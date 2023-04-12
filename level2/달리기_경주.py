def solution(players, callings):

    players_order = dict(zip(players,range(len(players))))
    order_players = dict(zip(range(len(players)),players))

    for call in callings:
        winner = call
        loser = order_players[players_order[call] - 1]
        players_order[winner],players_order[loser] = players_order[loser],players_order[winner]
        order_players[players_order[winner]],order_players[players_order[loser]] =\
            order_players[players_order[loser]], order_players[players_order[winner]]

    return list(order_players.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))