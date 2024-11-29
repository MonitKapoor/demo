def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial_for(num)
print(f"The factorial of {num} is {factorial_result}")



