# Function to find the largest of three numbers
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
#example usage
num1 = 25
num2 = 42
num3 = 19
result = largest_number(num1, num2, num3)
print("The largest number is:", result)
