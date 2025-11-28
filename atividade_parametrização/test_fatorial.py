import pytest
from fatorial import fatorial

@pytest.mark.parametrize('n, fatorial_desejado', [(0, 1), (3, 6), (5, 120)])
def test_fatorial(n, fatorial_desejado):
    if n == 0:
        assert 1
    else:
        fatorial_desejado = n * fatorial(n-1)
        assert fatorial(n) == fatorial_desejado
