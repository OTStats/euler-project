even_fibonacci_sum <- function(n){
  # Generate sequence ----.
  first = 0
  second = 1
  fibonacci_sequence = c(first, second)
  next_number = first + second
  
  while (next_number < n) {
    fibonacci_sequence = c(fibonacci_sequence, next_number)
    first = second
    second = next_number
    next_number = first + second
    }
  
  # Filter for even numbers ----.
  even_fibonacci_sequence = fibonacci_sequence[fibonacci_sequence %% 2 == 0]
  # Sum even numbers ----.
  sum(even_fibonacci_sequence)

  }

# [1] 4613732
