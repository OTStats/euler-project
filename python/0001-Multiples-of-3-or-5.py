# Multiples of 3 or 5
# 
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.


# Solution 1 -- using while loop
def multiple_3_or_5(sum_under = 1000):
  i = 1
  cumulative_sum = 0
  while i < sum_under:
    if i % 3 == 0 or i % 5 == 0: 
      cumulative_sum = i + cumulative_sum
      i +=1
    else:
      i += 1
  print(cumulative_sum)

multiple_3_or_5()
# 233168


# Solution 2 -- vector approach
def multiple_3_5_sum(less_than = 10):
  numbers_vector = list(range(less_than))
  # i = 0
  for i in range(less_than - 1): 
    if numbers_vector[i] % 3 == 0 or numbers_vector[i] % 5 == 0:
      
      numbers_vector[i] = numbers_vector[i]
    else: 
      numbers_vector[i] = 0
  print(sum(numbers_vector))

multiple_3_5_sum(1000)
# 233168
    


# Solution 3 -- vector approach and lambda function filter
def sum_3_5_multiples(less_than = 10):
  numbers_vector = list(range(less_than))
  
  # create function to detect multiples of 3 or 5
  multiple_3_or_5 = lambda x: x % 3 == 0 or x % 5 == 0
  # filter for multiples
  filtered_number_vector = list(filter(multiple_3_or_5, numbers_vector))
  
  print(sum(filtered_number_vector))

sum_3_5_multiples(1000)
# 233168
