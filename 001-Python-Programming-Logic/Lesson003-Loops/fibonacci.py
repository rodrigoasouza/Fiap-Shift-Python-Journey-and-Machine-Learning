def loop_fibonacci(fibonacci_range):
    initial = 0
    sequence = 1
    
    for _ in range(fibonacci_range):
        print(initial)
        num = initial + sequence
        initial = sequence
        sequence = num

def recursive_fibonacci(initial, sequence, fibonacci_range):
    fibonacci_range -= 1
    print(initial)

    if fibonacci_range > 0:
        num = initial + sequence
        recursive_fibonacci(sequence, num, fibonacci_range)

while True:
    fibonacci_method = input('Choose the fibonacci method([L] = Loop | [R] = Recursive) | Choose [C] to close: ').upper()

    if fibonacci_method == 'C':
        break
    else:
        fibonacci_range = int(input('Enter Fibonacci range: '))
        if fibonacci_method == 'L':
            loop_fibonacci(fibonacci_range)
        elif fibonacci_method == 'R':
            recursive_fibonacci(0, 1, fibonacci_range)



