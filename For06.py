def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    ans = 0
    for i in range(A,B):
        ans += i
        print(i)
    return ans
print(main(-6,8))