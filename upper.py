# Was thinking this as a fun function as it is simple
def upper(s):
    """ Number of upper case letters in a string. Solution for day 4.
    
    >>> upper("UpPer")
    2
    >>> upper("alllower")
    0
    
    """
    
    # Current number of upper case letters found
    upper = 0
    
    # Loop through all the letters in the string and if it is upper, increase
    for x in s:
        if x.isupper():
            upper += 1
    
    # Return upper
    return upper