library(tidyverse)

names <- read_lines("https://projecteuler.net/project/resources/p022_names.txt") %>% 
  gsub("[^[:alnum:] ]", " ", .) %>% 
  str_trim() %>% 
  str_split("\\s+") %>% 
  unlist() %>% 
  str_replace_all(., "\"", "")


  

tibble(names) %>% 
  arrange(names) %>% 
  mutate(id = row_number())
