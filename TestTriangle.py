# -*- coding: utf-8 -*-
"""
Updated Oct 3, 2024

@author: jrr
@author: rk
@author: mr
"""

"""
Below features all of the test cases I've used for this assignment.
"""

import unittest

# TEST FOR CIRCLECI

from Triangle import classify_triangle
# TEST
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')
            
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral', '3,3,3 should be Equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classify_triangle(4, 4, 4), 'Equilateral', '4,4,4 should be Equilateral')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(5, 2, 10), 'NotATriangle', '5, 2, 10 should be NotATriangle')

    def testZeros(self): 
        self.assertEqual(classify_triangle(0, 0, 1), 'InvalidInput', '0,0,1 should be invalid input')

    def testNegative(self): 
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidInput', '-1,1,1 should be invalid input')

    def test200(self): 
        self.assertEqual(classify_triangle(200, 200, 1), 'InvalidInput', '200,200,1 should be invalid input')

    def test201(self): 
        self.assertEqual(classify_triangle(201, 201, 1), 'InvalidInput', '201,201,1 should be invalid input')

    def test199(self): 
        self.assertEqual(classify_triangle(199, 199, 199), 'Equilateral', '199,199,199 should be Equilateral')

    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classify_triangle(10, 11, 12), 'Scalene', '10,11,12 is a Scalene triangle')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classify_triangle(7, 7, 4), 'Isosceles', '7,7,4 is an Isosceles triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classify_triangle(10, 10, 8), 'Isosceles', '10,10,8 is an Isosceles triangle')
        
    def testFloats(self): 
        self.assertEqual(classify_triangle(1.1, 1.1, 1.1), 'InvalidInput', '1.1,1.1,1.1 should be invalid input')

    def testLetters(self): 
        self.assertEqual(classify_triangle('x', 'y', 'z'), 'InvalidInput', 'x,y,z should be invalid input')

    def testBooleans(self): 
        self.assertEqual(classify_triangle(False, True, False), 'InvalidInput', 'False,True,False should be invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()