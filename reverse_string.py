# This function reverses a string manually
def reverse_str(s):
    rev = ""
    for ch in s:
        rev = ch + rev  
    return rev

# testing the function
word = "kiprotich"
print("Reversed:", reverse_str(word)) #reversed: chitorpik

word = "Mango"
print("Reversed:", reverse_str(word)) #reversed: ognaM
