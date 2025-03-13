age = int(input("Enter your age: "))

if age >= 10 and age <= 20:
    print("Your age is between 10 and 20.")
elif age < 10:
    print("Your age is less than 10.")
else:  # age > 20
    print("Your age is greater than 20.")