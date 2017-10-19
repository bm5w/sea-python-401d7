import pytest


PARAMS_TABLE = [
    (0, 0, 1), (1, 0, 2), (2, 0, 3), (3, 0, 4), (4, 0, 5),
    (0, 1, 2), (1, 1, 3), (2, 1, 4), (3, 1, 5), (4, 1, 6),
]


@pytest.mark.parametrize('m, n, result', PARAMS_TABLE)
def test_ackermann_m_n(m, n, result):
    from ackermann import ackermann
    assert ackermann(m, n) == result
