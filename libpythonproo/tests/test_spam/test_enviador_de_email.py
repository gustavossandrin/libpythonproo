import pytest

from libpythonproo.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gustavosandrindattein123@gmail.com', 'aleatoriateste@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gustavosandrindattein321@gmail.com',
        'Cursos Python Pro',
        'Primeira turma do curso'
     )
    assert remetente in resultado
