def print_values(num_a, num_b):
    """
    Prints the two numbers and their sum.

    Args:
        num_a (int): The first number.
        num_b (int): The second number.

    Returns:
        None: All values are displayed in console.
    """
    
    if isinstance(num_a, int) and isinstance(num_b, int):
        print(f"num_a: {num_a}")
        print(f"num_b: {num_b}")
        print(f"sum: {num_a + num_b}")
    else:
        raise TypeError('Inputs must be integer type.')