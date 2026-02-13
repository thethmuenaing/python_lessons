age = int(input('Enter your age: '))


if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print(f'You are now signed now!')
elif age < 0:
    print("You haven't been born yet!")
else:
    print(f'You must be above 18 to sign up')
