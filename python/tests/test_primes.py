import pytest

from python.tools import primes
from python.tools.primes import (
    partial_sieve,
    next_prime_by_trial_division,
    is_prime,
    TrialDivisionError,
    next_prime_by_sieve,
    prime_factors,
    product,
    nonprime_factors,
    better_nonprime_factors,
)


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (2, [2]),
        (3, [2, 3]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
    ],
)
@pytest.mark.parametrize(
    "func",
    [
        primes.eratosthenes_sieve,
        primes.eratosthenes_sieve2,
        primes.primes_by_trial_division,
        primes.sundaram_sieve,
        # primes.atkin_sieve,
    ],
)
def test_prime_finding_functions(func, input, expected_output):
    assert func(input) == expected_output


@pytest.mark.parametrize(
    "limit, known_primes, expected_result",
    [
        (0, [2, 3, 5], []),
        (1, [2, 3, 5], []),
        (2, [2, 3, 5], []),
        (7, [2], [3, 5, 7]),
        (9, [2], [3, 5, 7]),
        (19, [2, 3, 5], [7, 11, 13, 17, 19]),
        (20, [2, 3, 5], [7, 11, 13, 17, 19]),
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
    "input, expected_output",
    [
        ([2], 3),
        ([2, 3], 5),
        ([2, 3, 5, 7, 11, 13, 17, 19], 23),
    ],
)
def test_next_prime_by_sieve(input, expected_output):
    assert next_prime_by_sieve(input) == expected_output


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


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (0, {}),
        (1, {}),
        (2, {2: 1}),
        (4, {2: 2}),
        (6, {2: 1, 3: 1}),
        (7, {7: 1}),
        (8, {2: 3}),
        (24, {2: 3, 3: 1}),
        (25, {5: 2}),
        (144, {2: 4, 3: 2}),
        (43, {43: 1}),
    ],
)
def test_prime_factors(input, expected_output):
    result = prime_factors(input)
    assert result == expected_output
    if result:
        assert product(factor**power for factor, power in result.items()) == input


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (0, set()),
        (1, {1}),
        (2, {1, 2}),
        (10, {1, 2, 5, 10}),
        (20, {1, 2, 4, 5, 10, 20}),
        (27, {1, 3, 9, 27}),
        (50, {1, 2, 5, 10, 25, 50}),
        (43, {1, 43}),
    ],
)
@pytest.mark.parametrize("func", [nonprime_factors, better_nonprime_factors])
def test_nonprime_factors(func, input, expected_output):
    assert func(input) == expected_output
