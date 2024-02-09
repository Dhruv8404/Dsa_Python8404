
N = 10
if N == 10:
        fibonacci_series = []
        a, b = 0, 1  

        for i in range(N):
            fibonacci_series.append(a)
            a, b = b, a + b  

        print(f"The first {N} terms of the Fibonacci series are: {fibonacci_series}")


