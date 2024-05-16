def simulate(n, m):
    # Check if n and m are positive integers
    if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
        raise ValueError("n and m must be positive integers")

    # Check if n and m are within a reasonable range
    if n > 100 or m > 100:
        raise ValueError("n and m must be less than or equal to 100")

    # Initialize a counter to count the number of favorable outcomes
    favorable_outcomes = 0

    # Simulate rolling two fair dice with n and m sides respectively
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Check if the sum of the two rolls equals n
            if i + j == n:
                favorable_outcomes += 1

    # Calculate the probability of obtaining a sum of n
    probability = favorable_outcomes / (n * m)

    return probability

# Test the function with input values of n=6 and m=4
print(simulate(6, 4))
