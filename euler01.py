"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from typing import Callable
from utils import sum_all_neutrals


def euler1_v1(n: int, start: int = 1) -> int:
    """O(n) = n"""
    sum = 0
    for num in range(start,n):
        sum += num if (num % 3 == 0 or num % 5 == 0) else 0
    return sum


def euler1_v2(n: int) -> int:
    """O(n) = 1
    numbers we are looking for appears exacly 7 times every 15 natural numbers: 3,5,6,9,10,12,15, they sum to 60(TOP)
    """
    TOP = 60
    N = n - 1 # defining true n
    offset = N % 15
    num_of_steps = (N - offset) /15
    base = 7 * 15 * sum_all_neutrals(num_of_steps-1) # 7 numbers with base of 15 * number of bases
    result = TOP * num_of_steps + base
    result += euler1_v1(n, n - offset) # using O(n)=n method to calculate for bigest 0-14 numbers
    return result

def test_euler1(func: Callable) -> None:
    assert func(2) == 0
    assert func(10) == 23
    assert func(16) == 60
    assert func(1000) == 233168

if __name__ == "__main__": 
    test_euler1(euler1_v1)
    test_euler1(euler1_v2)
