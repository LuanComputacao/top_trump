from src.services.cards_services import check_turn


def test_player_um_deve_ganhar_se_tiver_maior_pontos_no_turno():
    result = check_turn(20, 10)
    expected = 1

    assert result == expected


def test_player_dois_deve_ganhar_se_tiver_maior_pontos_no_turno():
    result = check_turn(10, 20)
    expected = 2

    assert result == expected


def test_os_players_empatam_se_tiverem_pontos_iguais():
    result = check_turn(10, 10)
    expected = 0

    assert result == expected
