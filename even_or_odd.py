#this function that checks if a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# testting  the function
if __name__ == "__main__":
    n = 10
    print(n, "is", even_or_odd(n))
    # 10 is Even

    n = 13
    print(n, "is", even_or_odd(n))
    # 13 is Odd
