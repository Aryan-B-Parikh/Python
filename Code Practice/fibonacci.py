def fibonacci(n):
    """Generate first n numbers in the Fibonacci sequence."""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

if __name__ == "__main__":
    num = 10
    result = fibonacci(num)
    print(f"First {num} Fibonacci numbers: {result}")