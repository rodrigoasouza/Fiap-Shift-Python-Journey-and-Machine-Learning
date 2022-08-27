retry_count = 0

while True:
    retry_count+=1

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username.upper() == 'ADMIN' and password == '123':
        print('!!!   Successfully login   !!!')
        break
    else:
        print('!!!   Failed login   !!!')

print('There were {retry_count} attempts')