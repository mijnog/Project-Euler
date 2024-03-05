"""ChatGPT's Solution"""

def sum_of_multiples(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Example usage:
n = 1000
result = sum_of_multiples(n)
print("The sum of all multiples of 3 or 5 below", n, "is:", result)
