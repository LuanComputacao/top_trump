def format_player_name_to_upper(name: str):
    return name.upper()


def check_winner_game(turn_winner_sequence):
    players = {
        'p1': 0,
        'p2': 0
    }

    for winner in turn_winner_sequence:
        if winner == 1:
            players['p1'] += 1

        elif winner == 2:
            players['p2'] += 1

    if players['p1'] > players['p2']:
        return 1

    if players['p1'] < players['p2']:
        return 2

    return 0
