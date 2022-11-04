def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    ans = []
    for i in range(len(list1)):
        print(i)
        ans.append(list1[i].capitalize)
    return ans
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))
