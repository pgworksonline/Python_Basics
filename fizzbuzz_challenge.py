# Practice interview question
# If the number is divisible by 20, then print "twist".
# Otherwise, if the number is divisible by 15, then print nothing.
# Otherwise, if the number is divisible by 5, then print "fizz".
# Otherwise, if the number is divisible by 3, then print "buzz".
# Otherwise, print the number.

for x in range(100):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else: 
        print(x)

# Wrapped in a function for resusability
def fizzbuzz_twist(n):
    if n % 20 == 0:
        return "twist"
    elif n % 15 == 0:
        return None
    elif n % 5 == 0:
        return "fizz"
    elif n % 3 == 0:
        return "buzz"
    else:
        return n

for x in range(100):
    result = fizzbuzz_twist(x)
    if result is not None:
        print(result)

# Adding a unit test
assert fizzbuzz_twist(20) == "twist"
assert fizzbuzz_twist(15) is None
assert fizzbuzz_twist(10) == "fizz"
assert fizzbuzz_twist(9) == "buzz"
assert fizzbuzz_twist(7) == 7

# Dictionary of Rules
rules = {
    20: "twist",
    15: None,
    5: "fizz",
    3: "buzz"
}

def fizzbuzz_twist(n):
    for divisor, word in rules.items():
        if n % divisor == 0:
            return word
    return n
