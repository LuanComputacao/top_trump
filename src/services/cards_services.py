def check_turn(player1: float, player2: float):
    """Verificar qual dos dois jogadores tem maior pontos
    na caracteristica escolhida
    """
    if player1 > player2:
        return 1

    if player1 < player2:
        return 2

    return 0
