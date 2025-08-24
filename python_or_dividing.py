# One solution to writing arithmetic programs that might potentially divide by zero.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None   

def dividing():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        quotient = divide(a, b)

        if quotient is None:
            print("No result, division by zero attempted")
        else:
            print(f"The result of {a} divided by {b} is {quotient}")

    except ValueError:
        print("You must enter valid numbers")
