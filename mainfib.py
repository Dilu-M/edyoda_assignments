n = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1
fibonacci_series = []

for _ in range(n):
    fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci Series:")
print(" ".join(map(str, fibonacci_series)))
