# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

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


num <- 1:2000000

sum(num[unlist(map(num, is_prime))])
# [1] 142913828922
