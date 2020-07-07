# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

# I know this is a little unconventional, but it was the quickest way I could think to solve the problem (i.e. less than 10 seconds)
library(stringr)
scales::comma(2^1000) %>% 
  str_remove_all(",") %>% 
  str_split("") %>% 
  unlist() %>% 
  as.numeric() %>% 
  sum()
# [1] 1366
