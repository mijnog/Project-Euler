def fibonacci_sum_even(limit):
    # Initialize variables
    a, b = 1, 2
    even_sum = 0

    # Iterate until the current Fibonacci number exceeds the limit
    while a <= limit:
        # If the current number is even, add it to the sum
        if a % 2 == 0:
            even_sum += a
        # Generate the next Fibonacci number
        a, b = b, a + b

    return even_sum

# Set the limit to four million
limit = 4000000

# Calculate the sum of even-valued terms
result = fibonacci_sum_even(limit)
print("The sum of even-valued terms in the Fibonacci sequence up to", limit, "is:", result)

fibonacci_sum_even(limit)