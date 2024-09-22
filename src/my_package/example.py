def add_one(number):
    """
    Example of a simple function.

    Parameters
    ----------
    number: int, float, str

    Returns
    -------
    out: int, float, str
        The input value plus one. Raises TypeError if the input is not
        the expected type
    """

    if isinstance(number, (float, int)):
        result = number + 1
        return result
    elif isinstance(number, (str)):
        return number + '1'
    else:
        raise TypeError('Expecting an int, float or string.')
