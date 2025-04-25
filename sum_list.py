# This function adds up everything in the list
def sum_list(numbers):
    _sum = 0
    for n in numbers:
        _sum = _sum + n   # this keeps adding each number
    return _sum

# Testing the function
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("The sum of the list is:", sum_list(numbers))
    
