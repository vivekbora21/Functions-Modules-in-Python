def factorial(n):
    if n < 2:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
fac = factoria(num)
print(f"Factorial of {num} is: ",fac)
