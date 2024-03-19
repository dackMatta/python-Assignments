def generate_fibonacci(n):
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence.append(0)
        return fibonacci_sequence
    elif n == 2:
        fibonacci_sequence.extend([0, 1])
        return fibonacci_sequence
    else:
        fibonacci_sequence.extend([0, 1])
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

# Ask the user to input the value of n
n = int(input("Enter the number of terms in Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(n)

# Print the generated Fibonacci sequence
print("The Fibonacci sequence up to the", n, "th term is:", fibonacci_sequence)
