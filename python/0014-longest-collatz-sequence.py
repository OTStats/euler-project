# Longest Collatz sequence
# 
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.


def even_action(x):
  return(int(x/2))

def odd_action(x):
  return(int(3*x + 1))


num_final = 0
terms_final = 0

for i in range(1, 1000000):
  num_temp = i
  terms_temp = 0
  while num_temp > 1:
    
    terms_temp += 1
    if num_temp % 2 == 0:
      num_temp = even_action(num_temp)
    else: 
      num_temp = odd_action(num_temp)
  
  # Assign new values if there are more terms in the sequence for a number
  if terms_temp > terms_final:
     terms_final = terms_temp
     num_final = i
  
num_final
# 837799
  



