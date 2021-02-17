"""
Simple Matrix Utilities
stough, 202-
"""

import numpy as np

# Given an ndarray, returns a tuple of info...
def arr_info(arr):
    """
    arr_info(arr): return a tuple of shape, type, min, and max for the ndarray arr.
    """
    return arr.shape, arr.dtype, arr.min(), arr.max()


def make_linmap(inputrange=[0,1], outputrange=[0,255]):
    '''
    make_linmap(inputrange=[0,1], outputrange=[0,255]): return an anonymous function
    linear mapping from the inputrange to the outputrange.
    '''
    a,b = inputrange
    c,d = outputrange
    
    return lambda x: (1-((x-a)/(b-a)))*c + ((x-a)/(b-a))*d