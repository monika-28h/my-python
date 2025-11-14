#Write a Python program to create a list of 5 numbers entered by the user and print the list.
numbers = []
for i in range(5):
    n = int(input("Enter a number: "))
    numbers.append(n)

print("List:", numbers)
