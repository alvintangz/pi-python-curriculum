def findbiggest(T):
    """ Find the biggest number in a numbered list. Solution for day 3.
    
    >>> findbiggest([0, 1, 2])
    2
    >>> findbiggest([2, 7, 100, 3, 2])
    100
    >>> findbiggest([-1, -5, 5])
    5
    >>> findbiggest([-1, -6, -4])
    5
    
    """
    
    # Assume the biggest is the first number in the list
    biggest = T[0]
    
    # Loop through each number in the list
    # Can be for x in range(len(T)) with x being the index
    for x in T:
        # If the biggest number so far is smaller that the current number
        if(x > biggest):
            # Set the biggest number so far to the current number
            biggest = x
    
    # Return the biggest number
    return biggest;