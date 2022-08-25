age = int(input('Enter blood donor age: '))
weight = float(input('Enter blood donor weight: '))

if 18 <= age <= 65 and weight > 50.0:
    print('Could be a blood donor')
else:
    print('Cannot be a blood donor')
