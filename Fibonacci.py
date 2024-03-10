def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Example: Generate the first 10 terms of the Fibonacci sequence
n_terms = 10
fibonacci_sequence = generate_fibonacci(n_terms)
print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_sequence}")
