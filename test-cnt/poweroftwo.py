#computes the power of two that is the closest but smaller or equal to the given number n
import math

def find(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    m = int(n/2) + 1
    for i in range(1, m+1):
        if (math.pow(2,i) > n):
            return i - 1

def test_find():
    assert find(2) == 1
    assert find(10) == 3
    assert find(17) == 4

