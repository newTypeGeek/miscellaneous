
def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (gcd) from two
    non-negative integers using Euclidean algorithm.

    Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm

    Args:
        a (int): an non-negative integer
        b (int): an non-negative integer

    Returns:
        (int): greatest common divisor of a and b

    """
    if b == 0:
        return a

    r = a % b
    return gcd(b, r)


def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple from two non-negative
    integers using the following identity
    lcm(a,b) = (a * b) / gcd(a,b)


    Args:
        a (int): an non-negative integer
        b (int): an non-negative integer

    Returns:
        (int): least common multiple of a and b

    """
    if a == b == 0:
        return 0

    return (a*b) // gcd(a, b)


if __name__ == "__main__":

    cases = [
        [0, 0],
        [0, 1],
        [2, 4],
        [11, 17],
        [12345, 67890]
    ]

    for num1, num2 in cases:
        print("="*20)
        print(f"a = {num1},  b = {num2}")
        print(f"gcd = {gcd(num1, num2)}")
        print(f"lcm = {lcm(num1, num2)}")