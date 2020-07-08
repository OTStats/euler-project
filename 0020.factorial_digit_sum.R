# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

# -- Function for the sum of digits of a number
num_digit_sum <- function(x) sum(as.numeric(unlist(strsplit(as.character(x), split = ""))))

# --- First attempts kept giving a wrong answer (762) ---
# - First attempts
# library(magrittr)
# factorial(100) %>% 
#   scales::comma() %>%
#   str_remove_all(",") %>%
#   str_split("") %>%
#   unlist() %>%
#   as.numeric() %>%
#   sum()
# [1] 762
# -------------------------------------------------------.

# -- I had a feeling it had to do with the fact that I was dealing with a large integer, 
# of which I don't deal with on a day-to-day basis so I give it much thought at first.
# I came across the following answer on SO, which uses the {gmp} package to convert a 
# number into a "large integer" of class "bigz" (of which is a simple S3 class). 
# Perhaps something for me to look into later.
# https://stackoverflow.com/a/51497264/9855745
# install.packages("gmp")
library(gmp)

# 100 factorial as a "bigz", or large sized integer
fact_100 <- factorial(as.bigz(100))
num_digit_sum(fact_100)
# [1] 648

