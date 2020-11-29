def power(x: float, n: int) -> float:
    """
    Compute nth power of a number x using exponentiation by squaring
    Args:
        x (float): a real number
        n (int):  nth power

    Returns:
        (float): x ** n
    """
    if n < 0:
        return power(1/x, -n)

    if n == 0:
        return 1

    if n == 1:
        return x

    if n % 2 == 0:
        return power(x*x, n//2)

    if n % 2 == 1:
        return x * power(x*x, (n-1)//2)


if __name__ == "__main__":
    a = 1024
    b = 3721
    print(power(a,b))