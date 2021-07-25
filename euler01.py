"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math

from typing import Callable, List, Tuple

from utils import sum_all_neutrals


def euler1_v1(n: int, start: int = 1) -> int:
    """O(n) = n"""
    sum = 0
    for num in range(start, n):
        sum += num if (num % 3 == 0 or num % 5 == 0) else 0
    return sum


def euler1_v2(n: int) -> int:
    """O(n) = 1
    numbers we are looking for appears exacly 7 times every 15 natural numbers: 3,5,6,9,10,12,15, they sum to 60(TOP)
    """
    sum_of_denominators = 60
    num_of_denominators = 7
    common_denominator = 15
    N = n - 1  # defining true n
    offset = N % common_denominator
    num_of_steps = int((N - offset) / common_denominator)
    base = (
        num_of_denominators * common_denominator * sum_all_neutrals(num_of_steps - 1)
    )  # 7 numbers with base of 15 * number of bases
    result = sum_of_denominators * num_of_steps + base
    result += euler1_v1(
        n, n - offset
    )  # using O(n)=n method to calculate for bigest 0-14 numbers
    return result


def test_euler1(func: Callable) -> None:
    assert func(2) == 0
    assert func(10) == 23
    assert func(16) == 60
    assert func(1000) == 233168


def euler1_generalization(*, n: int, m: Tuple[int, ...], reduce_m: bool = False):
    def _reduce_m(m: Tuple[int, ...]) -> Tuple[int, ...]:
        result = []
        for i in range(len(m)):
            good = True
            for e in m[: -i - 1]:
                if m[-i - 1] % e == 0:
                    good = False
                    break
            if good:
                result.append(m[-i - 1])
        return tuple(result)

    def _find_step(*, m: Tuple[int, ...]) -> Tuple[int, int, int]:
        common_denominator: int = math.prod(m)  # functools.reduce(operator.mul, m, 1)
        denominators: List[int] = []
        for neutral in range(1, common_denominator + 1):
            if any(neutral % _m == 0 for _m in m):
                denominators.append(neutral)
        return common_denominator, sum(denominators), len(denominators)

    def _find_numer_of_steps(*, n: int, common_denominator: int) -> Tuple[int, int]:
        offset = n % common_denominator
        num_of_steps = int((n - offset) / common_denominator)
        return num_of_steps, offset

    def _cal_offset(*, n: int, m: Tuple[int, ...], offset: int) -> int:
        sum = 0
        for num in range(n - offset, n):
            sum += num if any(num % _m == 0 for _m in m) else 0
        return sum

    # I can still optimise m (3,5,6) gives the same results as (3,5) but it takes longer to compute
    # if the smaller numer is a denominator of a bigger bigger can be removed from m
    if reduce_m:
        m = _reduce_m(m)

    common_denominator, sum_of_denominators, num_of_denominators = _find_step(m=m)
    num_of_steps, offset = _find_numer_of_steps(
        n=n - 1, common_denominator=common_denominator
    )

    res = (
        sum_of_denominators * num_of_steps
        + num_of_denominators * common_denominator * sum_all_neutrals(num_of_steps - 1)
    )
    res += _cal_offset(n=n, m=m, offset=offset)

    return res


def test_euler1_generalization() -> None:
    assert euler1_generalization(n=16, m=(3, 5)) == 60
    assert euler1_generalization(n=2, m=(3, 5)) == 0
    assert euler1_generalization(n=10, m=(3, 5)) == 23
    assert euler1_generalization(n=31, m=(3, 5)) == euler1_v2(31)
    assert euler1_generalization(n=1000, m=(3, 5)) == 233168
    assert euler1_generalization(n=1000, m=(3, 5, 6)) == 233168
    assert euler1_generalization(
        n=368900, m=(3, 5, 6, 7, 13, 15), reduce_m=True
    ) == euler1_generalization(n=368900, m=(3, 5, 6, 7, 13, 15))


if __name__ == "__main__":
    # test_euler1(euler1_v1)
    # test_euler1(euler1_v2)
    test_euler1_generalization()
