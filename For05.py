def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    ans = []
    for i in range(A,B+1):
        ans.append(i)
    
    return ans[::-1]