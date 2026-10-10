def get_score(player):
    """Returns a player's score"""
    return player[1]


players = [["Ada", 4300], ["Margaret", 9800], ["Guido", 7200], ["Linus", 8650]]

for player in sorted(players, key=get_score, reverse=True):
    print(f"{player[0]:<10} {player[1]:>5}")
