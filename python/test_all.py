import pytest

from python import puzzles


@pytest.mark.parametrize(
    "func, expected_answer", [
        (puzzles.euler1.euler1, 233168),
        (puzzles.euler2.euler2, 4613732),
        (puzzles.euler3.euler3, 6857),
        (puzzles.euler4.euler4, 906609),
        (puzzles.euler5.euler5, 232792560),
        (puzzles.euler6.euler6, 25164150),
        (puzzles.euler7.euler7, 104743),
        (puzzles.euler8.euler8, 23514624000),
        (puzzles.euler9.euler9, 31875000),
        (puzzles.euler10.euler10, 142913828922),
        (puzzles.euler11.euler11, 70600674),
        (puzzles.euler12.euler12, 76576500),
        (puzzles.euler13.euler13, 5537376230),
        (puzzles.euler14.euler14, 837799),
        (puzzles.euler15.euler15, 137846528820),
        (puzzles.euler16.euler16, 1366),
        (puzzles.euler17.euler17, 21124),
        (puzzles.euler18.euler18, 1074),
        (puzzles.euler19.euler19, 171),
        (puzzles.euler20.euler20, 648),
        (puzzles.euler21.euler21, 31626),
        (puzzles.euler22.euler22, 871198282),
        (puzzles.euler23.euler23, 4179871),
        (puzzles.euler24.euler24, 2783915460),
        (puzzles.euler25.euler25, 4782),
        (puzzles.euler26.euler26, 983),
        # (puzzles.euler27.euler27, -59231),
        (puzzles.euler28.euler28, 669171001),
        (puzzles.euler29.euler29, 9183),
        (puzzles.euler30.euler30, 443839),
        # (puzzles.euler31.euler31, 73682),
        (puzzles.euler32.euler32, 45228),
        (puzzles.euler33.euler33, 100),
        # (puzzles.euler34.euler34, 40730),
        # (puzzles.euler35.euler35, 55),
        # (puzzles.euler36.euler36, 872187),
        # (puzzles.euler37.euler37, 748317),
        # (puzzles.euler38.euler38, 932718654),
        # (puzzles.euler39.euler39, 840),
        # (puzzles.euler40.euler40, 210),
        # (puzzles.euler41.euler41, 7652413),
        # (puzzles.euler42.euler42, 162),
        # (puzzles.euler43.euler43, 16695334890),
    ]
)
def test_all(func, expected_answer):
    assert func() == expected_answer