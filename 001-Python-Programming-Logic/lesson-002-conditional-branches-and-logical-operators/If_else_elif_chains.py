print('PASSENGER VALIDATOR')
old = int(input('Enter your age: '))

if old < 16:
    print('Passenger cannot vote or board')
elif old < 18:
    print("The passenger's vote is optional and he can board")
else:
    print("The passenger must vote and can board")
