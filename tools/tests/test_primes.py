import pytest

from tools.primes import sieve_primes, partial_sieve


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    ],
)
def test_sieve_primes(input, expected_output):
    assert sieve_primes(input) == expected_output


@pytest.mark.parametrize(
    "limit, known_primes, expected_result",
    [
        (0, None, []),
        (1, None, []),
        (2, None, [2]),
        (19, None, [2, 3, 5, 7, 11, 13, 17, 19]),
        (20, None, [2, 3, 5, 7, 11, 13, 17, 19]),
        (0, [2, 3, 5], []),
        (1, [2, 3, 5], []),
        (2, [2, 3, 5], [2]),
        (19, [2, 3, 5], [2, 3, 5, 7, 11, 13, 17, 19]),
        (20, [2, 3, 5], [2, 3, 5, 7, 11, 13, 17, 19]),
    ],
)
def test_partial_sieve(limit, known_primes, expected_result):
    assert partial_sieve(limit=limit, primes=known_primes) == expected_result
