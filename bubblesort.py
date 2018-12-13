def bubblesort(T):
    """ Bubble sort. Solution for day 3.
    
    >>> bubblesort([0, 1, 2, 3, 4, 5, 6])
    [0, 1, 2, 3, 4, 5, 6]
    >>> bubblesort([-8, 9, 4, 5, 2])
    [-8, 2, 4, 5, 9]
    
    """
    
    # n being the length of list T
    n = len(T)
    
    # Loop through the whole list
    for x in range(n):
        # Last x items in the list are already in place
        for y in range(n-x-1):
            
            # Switch the items in the list if the previous was greater
            if(T[y] > T[y+1]):
                T[y], T[y+1] = T[y+1], T[y]
    
    # Return the list
    return T