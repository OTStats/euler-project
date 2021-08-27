# Special Pythagorean triplet
# 
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 1000):
  for b in range(1, 1000):
    c = (1000 - a) - b
    if a < b < c:
      if a**2 + b**2 == c**2:
        abc_product = a * b * c
        print("a:" + str(a))
        print("b:" + str(b))
        print("c:" + str(c))
        print("Product of a, b, and c: " + "{:,}".format(abc_product))


# Resource found: 
# https://codereview.stackexchange.com/questions/224132/project-euler-problem-9-pythagorean-triplet
# 
# def get_triplet():
#     for c in range(2, 1000):
#         for b in range(2, c):
#             a = 1000 - c - b
#             if a ** 2 + b ** 2 == c ** 2:
#                 return 'n1 = %s\nn2 = ' \
#                        '%s\nn3 = %s\nproduct = %s' \
#                        % (a, b, c, a * b * c)
# 
# 
# if __name__ == '__main__':
#     print(get_triplet())

