try:
    age = int(input("What is your age? "))

    if 0 <= age <= 9:
        print("You are a child!")

    elif 10 <= age <= 18:
        print("You are an adolescent!")

    elif 19 <= age <= 65:
        print("You are an adult.")

    elif age > 65:
        print("You are vintage!")

    else:
        print("Age cannot be negative.")

except ValueError:
    print("You must enter a valid number")
