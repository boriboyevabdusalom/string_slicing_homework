def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1 = s[1:-1]
    return s1
print(main("hello"))
print(main("positive"))