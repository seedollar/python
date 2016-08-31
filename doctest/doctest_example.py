# Example of how to use doctest package to write tests within the docstring section.
def capitalize_str(text):
    """
    >>> capitalize_str('cat')
    'Cat'
    >>> capitalize_str('cat in hat')
    'Cat In Hat'
    """
    from string import capwords
    return capwords(text)

if __name__ == '__main__':
    import doctest
    doctest.testmod()