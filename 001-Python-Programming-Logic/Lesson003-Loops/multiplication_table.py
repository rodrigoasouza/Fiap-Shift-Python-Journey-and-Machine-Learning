value = int(input('Insert number: '))
multiplication_range = int(input('Insert range: '))

for i in range(1, multiplication_range):
    multiplication = i * value
    
    print(f'{value} x {i} = {multiplication}')
