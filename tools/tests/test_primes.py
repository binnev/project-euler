import pytest

from tools.primes import (
    sieve_primes,
    partial_sieve,
    next_prime_by_trial_division,
    is_prime,
    TrialDivisionError,
)


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


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ([2], 3),
        ([2, 3], 5),
        ([2, 3, 5, 7, 11, 13, 17, 19], 23),
    ],
)
def test_next_prime_by_trial_division(input, expected_output):
    assert next_prime_by_trial_division(input) == expected_output


@pytest.mark.parametrize(
    "n, primes, expected_result",
    [
        (2, [2], True),
        (4, [2], False),
        (23, [2, 3, 5, 7, 11, 13], True),
        (4, [2, 3, 5, 7, 11, 13], False),
        (144, [2, 3, 5, 7, 11, 13], False),
        (10000000, [2, 3, 5], TrialDivisionError()),
    ],
)
def test_is_prime(n, primes, expected_result):
    if isinstance(expected_result, Exception):
        exception_class = expected_result.__class__
        with pytest.raises(exception_class):
            is_prime(n, primes)
    else:
        assert is_prime(n, primes) == expected_result
