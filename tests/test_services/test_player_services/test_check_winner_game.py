from src.services.player_services import check_winner_game


def test_player_um_deve_ganhar_por_mais_turnos_ganhos():
    given = (2, 1, 0, 1)

    result = check_winner_game(given)
    expected = 1

    assert result == expected


def test_player_dois_deve_ganhar_por_mais_turnos_ganhos():
    given = (2, 2, 0, 1)

    result = check_winner_game(given)
    expected = 2

    assert result == expected


def test_deve_haver_empate_para_pontuacoes_iguais():
    given = (2, 2, 1, 1)

    result = check_winner_game(given)
    expected = 0

    assert result == expected
