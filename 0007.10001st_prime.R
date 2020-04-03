# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

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


num <- 1:200000

num[unlist(map(num, is_prime))][10001]
#[1] 104743
