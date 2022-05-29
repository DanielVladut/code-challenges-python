# given a series of sequential numbers but not necesarily ordered in the series, 
# find the sum of duplicates and the ones that are missing 
#[1,2,3,4,4,6] = 9
#[2,6,5,3,3,7,10,9,9] = 24
#[2,3,3,5,6,6,9,9,11,11] = 58

def sum(nums):
    s = sorted(nums)
    sum = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1] + 1:
            sum = sum + s[i] + s[i-1] + 1 
            s[i] = s[i-1] + 1
    return sum

def test_sum():
    assert sum([1,2,3,4,4,6]) == 9
    assert sum([2,6,5,3,3,7,10,9,9]) == 24
    assert sum([2,3,3,5,6,6,9,9,11,11]) == 58

