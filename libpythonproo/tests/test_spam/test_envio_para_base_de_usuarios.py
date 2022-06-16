from unittest.mock import Mock

import pytest

from libpythonproo.spam.main import EnviadorDeSpam
from libpythonproo.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com'),
            Usuario(nome='guilherme', email='gustavosandrindattein123@gmail.com')
        ],
        [
            Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavossandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavo123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with == (
        'gustavo123@gmail.com',
        'gustavosandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
     )
