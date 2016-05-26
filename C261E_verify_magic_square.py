from math import sqrt, ceil
from pprint import pprint
import sys

def verify(nums):
    total = sum(nums) / sqrt(len(nums))
    dim = int(sqrt(len(nums)))
    nums = [nums[i*dim:i*dim+dim] for i in range(dim)]
    
    for x in range(dim):
        # Row
        if sum(nums[x]) != total: return False
        # Column
        if sum(nums[i][x] for i in range(dim)) != total: return False
    # Diagonals
    if sum(nums[i][i] for i in range(dim)) != total: return False
    if sum(nums[i][dim-1-i] for i in range(dim)) != total: return False
    
    return True

def complete(nums):
    dim = ceil(sqrt(len(nums)))
    square = [nums[i*dim:i*dim+dim] for i in range(dim-1)]
    total = sum(square[0])
    last_row = [total - sum(square[i][x] for i in range(dim-1)) for x in range(dim)]
    return verify(nums + last_row)

if __name__ == '__main__':
    inputs = (
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [3, 8, 7, 10, 6, 2, 5, 4, 9],
        [3, 5, 7, 8, 1, 6, 4, 9, 2],
        [8, 1, 6, 7, 5, 3, 4, 9, 2],
        [1, 14, 8, 11, 15, 4, 10, 5, 12, 7, 13, 2, 6, 9, 3, 16],
        [1, 14, 8, 11, 12, 7, 13, 2, 15, 4, 10, 5, 6, 9, 3, 16])

    for nums in inputs:
        print(verify(nums))
    inputs = (
        [8, 1, 6, 3, 5, 7],
        [3, 5, 7, 8, 1, 6],
        [1, 14, 8, 11, 15, 4, 10, 5, 12, 7, 13, 2],
        [1, 14, 8, 11, 12, 7, 13, 2, 15, 4, 10, 5]
        )
    for nums in inputs:
        print(complete(nums))
