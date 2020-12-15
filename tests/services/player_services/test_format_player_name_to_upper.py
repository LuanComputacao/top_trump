from src.services.player_services import format_player_name_to_upper


def test_deve_colocar_nome_com_caracteres_alfabeticos_em_maiusculo():
    result = format_player_name_to_upper('aWdF')
    expected = 'AWDF'

    assert result == expected
