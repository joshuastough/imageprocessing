"""
Simple Matrix Utilities
stough, 202-
"""

import numpy as np

# Given an ndarray, returns a tuple of info...
def arr_info(arr):
    return arr.shape, arr.dtype, arr.min(), arr.max()