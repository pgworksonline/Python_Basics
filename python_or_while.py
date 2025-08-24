# Using the 'or' operator in action
number = int(input("Please enter a number between 1 and 10: "))
while (number < 1 or number > 10):
    number = int(input("Please enter a number between 1 and 10: "))

print(f"The number entered was {number}")
