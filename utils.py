def sum_all_neutrals(n: int) -> int:
    """Sums all neutral numbers from 1 to n"""
    return int((n + 1) * n / 2)


def test_sum_all_neutrals() -> None:
    assert sum_all_neutrals(1) == sum([1])
    assert sum_all_neutrals(9) == sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert sum_all_neutrals(9) == sum(range(10))
    assert sum_all_neutrals(20) == sum(range(21))
    assert sum_all_neutrals(100) == sum(range(101))
    assert sum_all_neutrals(6666) == sum(range(6667))


if __name__ == "__main__":
    test_sum_all_neutrals()
