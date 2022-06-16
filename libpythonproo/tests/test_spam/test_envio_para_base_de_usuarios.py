from libpythonproo.spam.enviador_de_email import Enviador
from libpythonproo.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao,):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gustavossandrindattein123@gmail.com',
        'curso python pro',
        'confira os módulos fantásticos'
    )