# this function calculates the factorial of a number using a loop
def factorial(n):
    result = 1
    if n < 0:
        return "Factorial doesn't work for negative numbers"
    
    for i in range(1, n + 1):
        result = result * i
    return result

# testing the function
print("Factorial of 5:", factorial(5)) # 120
print("Factorial of 0:", factorial(0)) # 1
print("Factorial of -3:", factorial(-3)) # Factorial doesn't work for negative numbers
