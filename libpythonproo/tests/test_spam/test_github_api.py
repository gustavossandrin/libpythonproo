from unittest.mock import Mock

from libpythonproo import github_api


def teste_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'gustavossandrin', 'id': 94086373, 'node_id': 'U_kgDOBZuk5Q',
        'avatar_url': 'https://avatars.githubusercontent.com/u/94086373?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('gustavossandrin')
    assert 'https://avatars.githubusercontent.com/u/94086373?v=4' == url
