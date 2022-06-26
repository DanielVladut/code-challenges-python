# https://github.com/blakeembrey/code-problems/tree/master/problems/array-pair-sum


def get_pairs(n, array):
    result = []
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            x = array[i]
            y = array[j]
            if x != y and x + y == n:
                tuple = (x,y) if x < y else (y,x)
                if not tuple in result:
                    result.append(tuple)
    return result

def test_get_pairs():
    assert get_pairs(3,[1,2,3]) == [(1,2)]
    assert get_pairs(10, [3, 4, 5, 6, 7])  == [(3, 7), (4, 6)]
    assert get_pairs(8, [3, 4, 5, 4, 4]) == [(3, 5)]
    assert get_pairs(9, [3, 4, 5, 4, 5]) == [(4, 5)]
    assert get_pairs(10, [3, 5, 6, 8]) == []