# Problem 15 : Lattice Paths

import math

def grid(grid_size):
    return math.comb(2 * grid_size, grid_size)

print(grid(20))