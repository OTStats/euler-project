# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# Import libraries
from itertools import product
import numpy

# Create list of numbers in the 900s, and a reversed copy
three_digit_nums = list(range(900,1000))
rev_three_digit_nums = list(range(900, 1000))[::-1]

# Generate all products of number combinations from my two lists
# Resource: https://stackoverflow.com/a/48143493/9855745
all_product_combos = [x * y for x, y in product(three_digit_nums, rev_three_digit_nums)]
# Get unique product values
unique_products = list(numpy.unique(all_product_combos))

# Create empty output array
out = []

# Loop through unique products to find whether the number is a palindrome, if the number
# is a palindrome then append to the out array
for i in range(len(unique_products)):
  if str(unique_products[i]) == str(unique_products[i])[::-1]:
    out.append(unique_products[i])

# What is the max number in the out array?
max(out)
# 906609
