import pytest
import server


@pytest.fixture
def api(monkeypatch):
    test_dogs = [{'id': 1, 'name': 'Mochi'}, {'id': 2, 'name': 'Masha'}]
    monkeypatch.setattr(server, "dogs", test_dogs)
    api = server.app.test_client()
    return api

# if __name__ == '__main__':
#     pytest.main(['-v','--cov=.', '--cov-report=html'])


