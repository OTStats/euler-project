# 3
# Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

is_prime <- function(x) {
  if (x == 1) {
    flag <- FALSE
  }
  if (x == 2 | x == 3) {
    flag <- TRUE
  } else {
    flag <- !any(x %% 2:floor(sqrt(x)) == 0)
  }
  return(flag)
}

max_prime_factor <- function(x) {
  potential_factors <- 2:floor(sqrt(x))
  factors <- potential_factors[x %% potential_factors == 0]
  prime_factors <- factors[unlist(lapply(factors, is_prime))]
  max(prime_factors)
}

#max_prime_factor(13195)
# [1] 29

max_prime_factor(600851475143)
# [1] 6857
