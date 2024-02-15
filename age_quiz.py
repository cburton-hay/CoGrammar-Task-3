age = input("How old are you?")
age = int(age)
if age > 100: # Starting at the upper limit of the age so working through conditions backwards from 100 as it'll stop at the first statement that is true.
    print("Sorry,you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill!")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for a kiddie discount.")
else:
    print("Age is just a number.")