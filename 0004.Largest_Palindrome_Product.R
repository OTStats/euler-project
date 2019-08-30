# Largest product of two 3-digit numbers, we'll start with numbers in the 900s
m <- matrix(900:999, nrow = 1)
m <- t(m) %*% m  # matrix multiplication

possible <- as.vector(m)
possible <- unique(sort(candidate, decreasing = TRUE))  # keep unique possiblities; in descending order

palindrome <- function(x) {
  x <- as.character(x)
  forward <- unlist(strsplit(x, split = ""))
  backward <- rev(forward)
  palindrome_number <- all(forward == backward)
  return(palindrome_number)
}

max_palindrome <- 0
i <- 1
n <- length(possible)
while (i <= n) {
    if (palindrome(possible[i])){
      max_palindrome <- possible[i]
      break
    }
  i <- i + 1
}

# [1] 819918
