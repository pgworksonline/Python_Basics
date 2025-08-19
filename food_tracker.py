from time import sleep

print()
print("--------------")
print("Welcome to the food tracker APP!")
print("--------------")
print()

weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri']
answers = []

for i in weekdays:
    print (f'Did you eat healthy on {i}')
    answer = input("'Y' or 'N': ").upper()
    answers.append(answer)

print()
print('Calculating your answers...')
sleep(3)

if len(answers) == 6:
    print('You earned the cake and ice cream this Saturday')
elif len(answers) == 5:
    print("You earned just the cake this Saturday")
else:
    print("You should probably try harder next week. No cake or ice cream for you!")
