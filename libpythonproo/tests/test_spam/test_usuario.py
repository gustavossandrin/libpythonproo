from libpythonproo.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='gustavo', email='gustavosandrindattein123@gmail.com'),
        Usuario(nome='guilherme', email='gustavosandrindattein123@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
