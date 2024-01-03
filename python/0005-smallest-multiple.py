# import math
# def flag_prime(x):
#   if x == 1:
#     flag = False
#   # Set the "base" prime numbers
#   if x == 2 | x == 3:
#     flag = True
#   # 
#   else:
#     possible_factors = list(range(2, int(math.sqrt(x)) + 1))
#     n_possible_factors = len(list(filter(lambda y: x % y == 0, possible_factors)))
#     if n_possible_factors == 0:
#       flag = True
#     else: 
#       flag = False
#   return(flag)
# 
# filter(flag_prime, list(range(1, 20)))
# 
# 
# # Prime numbers less than 20: 2, 3, 5, 7, 11, 13, 17, 19
# prime_product = 2*3*5*7*11*13*17*19
# 
# flag = False
# i = prime_product
# output = []
# while not flag:
#   if (i & prime_product == 0) and (i % 2520 == 0) and (i % 9 ==0) & (i % 16 == 0): 
#     flag = True
#     output = i
#   else:
#     i += 1


# Prime numbers less than 20: 2, 3, 5, 7, 11, 13, 17, 19 
# - Lowest multiple must at least the product of the prime numbers
# 
# Remaining numbers less than 20: 4, 6, 8, 9, 12, 14, 15, 16, 18, 20
#  - ^ what are their composites?
#     [2*2], [2*3], [2*2*2], [3*3], [2*2*3], [2*7], [3*5], [2*2*2*2], [2*3*3], [2*2*5]
# 

2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19



# Other Resource
# -https://euler.beerbaronbill.com/en/latest/solutions/5.html
