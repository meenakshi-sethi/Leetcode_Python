# LC 70 Climbing Stairs

# Brute Force approach : Recursive
def climbStairsBF(n):
    if n <= 2:
        return n
    return climbStairsBF(n-1) + climbStairsBF(n-2)

'''think of decision tree''' 

# Approach Bottom Up DP Optimised

def climbStairsOP(n):
    one, two = 1, 1

    for i in range(n -1):
        temp = one
        one = one + two
        two = temp
    return one


def test_climbStairs():
    # Small values (both functions should work)
    assert climbStairsBF(1) == 1   # Only 1 way → [1]
    assert climbStairsOP(1) == 1

    assert climbStairsBF(2) == 2   # [1+1], [2]
    assert climbStairsOP(2) == 2

    assert climbStairsBF(3) == 3   # [1+1+1], [1+2], [2+1]
    assert climbStairsOP(3) == 3

    assert climbStairsBF(4) == 5   # 5 ways
    assert climbStairsOP(4) == 5

    # Larger values (only optimized, brute force would be too slow)
    assert climbStairsOP(5) == 8
    assert climbStairsOP(6) == 13
    assert climbStairsOP(10) == 89
    assert climbStairsOP(20) == 10946

    print("All test cases passed!")

# Run tests
test_climbStairs()
