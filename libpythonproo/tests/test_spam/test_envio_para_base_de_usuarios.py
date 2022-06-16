import pytest

from libpythonproo.spam.enviador_de_email import Enviador
from libpythonproo.spam.main import EnviadorDeSpam
from libpythonproo.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavossandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavo123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'gustavo123@gmail.com',
        'gustavosandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )
