from unittest.mock import Mock

import pytest

from libpythonproo import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/94086373?v=4'
    resp_mock.json.return_value = {
        'login': 'gustavossandrin', 'id': 94086373, 'node_id': 'U_kgDOBZuk5Q',
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonproo.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('gustavossandrin')
    assert avatar_url == url


def teste_buscar_avatar_intregracao():
    url = github_api.buscar_avatar('gustavossandrin')
    assert 'https://avatars.githubusercontent.com/u/94086373?v=4' == url
