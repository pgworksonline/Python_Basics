## Using the 'or' operator in action

def answer():
    ans = input("Do you want a puppy? (yes/no): ")
    if ans.lower() == 'yes' or ans.lower() == 'y':
        print(f"When asked if you wanted a new puppy, you answered {ans}")

    elif ans.lower() == 'no' or ans.lower() == "n":
        print(f"When asked if you wanted a new puppy, you said {ans}")

answer()


def my_range(x):
    if x < 20 or x > 40:
        print("Outside")
    else:
        print("Inside")

my_range(20)
