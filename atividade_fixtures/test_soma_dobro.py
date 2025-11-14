import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def soma_dobro(sample_list):
    return sum(x * 2 for x in sample_list)

@pytest.fixture
def test_soma_dobro(soma_dobro):
    assert soma_dobro == 30

