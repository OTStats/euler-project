# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# -- Load libraries
library(tidyverse)

crossing(a = 1:999, 
         b = 1:999) %>% 
  filter(a < b) %>% 
  mutate(c = 1000 - a - b) %>% 
  filter(b < c) %>% 
  filter(a^2 + b^2 == c^2) %>% 
  mutate(abc_product = prod(a, b, c))
# # A tibble: 1 x 4
#        a     b     c abc_product
#    <int> <int> <dbl>       <dbl>
#  1   200   375   425    31875000
