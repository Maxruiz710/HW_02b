# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Oct 28, 2024

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: mr
"""

def classify_triangle(side_a, side_b, side_c):

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type)" returns True if the object is of the specified type
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if side_a >= 200 or side_b >= 200 or side_c >= 200:
        return 'InvalidInput'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'

    # the sum of any two sides must be strictly greater than the third side
    # if the specified shape is not a triangle
    if (side_a >= (side_b + side_c)) or (side_b >= (side_a + side_c)) or (side_c >= (side_a + side_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (side_a ** 2 + side_b ** 2 == side_c ** 2) or (side_a ** 2 + side_c ** 2 == side_b ** 2) or (side_b ** 2 + side_c ** 2 == side_a ** 2):
        return 'Right'
    if side_a != side_b and side_b != side_c and side_a != side_c:
        return 'Scalene'
    return 'Isosceles'