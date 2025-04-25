# this function adds up all digits in a number
def digit_sum(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

# testing the function
print("Sum of digits:", digit_sum(492)) # 15
print("Sum of digits:", digit_sum(123456789)) # 45
print("Sum of digits:", digit_sum(0)) # 0
