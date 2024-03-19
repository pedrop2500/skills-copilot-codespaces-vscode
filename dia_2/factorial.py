def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# imprimir factorial de 5
print(factorial(5))

