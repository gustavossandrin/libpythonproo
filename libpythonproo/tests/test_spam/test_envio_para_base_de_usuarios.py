import pytest

from libpythonproo.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavossandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados
