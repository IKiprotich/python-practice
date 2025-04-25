# this function implements the the recursive version of factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# testing the function
print("Recursive factorial of 4:", fact(4)) # 24
print("Recursive factorial of 0:", fact(0)) # 1
print("Recursive factorial of -3:", fact(-3)) # 1
