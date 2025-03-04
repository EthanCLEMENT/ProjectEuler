# Problem 67 : Maximum Path Sum II

def read_triangle(filename):
    with open(filename, 'r') as file:
        triangle = [list(map(int, line.split())) for line in file]
    return triangle

filename = "triangle.txt"  
triangle = read_triangle(filename)

import copy

def sum_path(triangle):
    tri = copy.deepcopy(triangle)  
    for i in range(len(tri) - 2, -1, -1):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
    return tri[0][0]

print(sum_path(triangle))

