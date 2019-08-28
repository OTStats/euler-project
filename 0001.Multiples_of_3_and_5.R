name <- function(less_than = 10) {

  vec <- 1:(less_than - 1)
  for (i in 1:length(vec)) {
    if (vec[i] %% 3 == 0 | vec[i] %% 5 == 0) {
      
    } else {
      vec[i] <- 0
    }
  }
  sum(vec)
}
