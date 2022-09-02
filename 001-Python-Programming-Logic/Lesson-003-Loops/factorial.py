def calc_factorial(factorial):
    if factorial == 0:
        message = '0! = 1'
    elif factorial == 1:
        message = '1! = 1'
    else:
        message = f'{factorial}! = {factorial}'
        aux = factorial - 1

        for _ in range(factorial - 1):
            factorial *= aux
            message += f'.{aux}'
            aux -= 1

        message += f' = {factorial}'
    
    print(message)

up_to = int(input('Calculate factorial up to: '))

for i in range(up_to + 1):
    calc_factorial(i)
