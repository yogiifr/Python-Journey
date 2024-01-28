'''
 is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.
'''

import math

ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2+bc**2)
theta = round(math.asin(ab/ac)*180/math.pi)

print(f"{theta}\u00b0")