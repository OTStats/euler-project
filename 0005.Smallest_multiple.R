# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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


prime_facts <- function(x) {
  potential_factors <- 2:floor(sqrt(x))
  factors <- potential_factors[x %% potential_factors == 0]
  prime_factors <- factors[unlist(lapply(factors, is_prime))]
  prime_factors
}


all <- 1:20

prime <- all[map(1:20, is_prime) %>% unlist()]
length(prime)
prod(prime) * length(prime)
