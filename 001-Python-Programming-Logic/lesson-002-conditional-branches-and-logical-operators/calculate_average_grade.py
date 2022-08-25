CONGRATULATIONS = "Congratulations, you've been approved!"
FAILED = 'You failed'

def validate(result, firstTime):
    if result >= 7:
        print(CONGRATULATIONS)
    elif firstTime and result >= 3:
        exam = float(input('Enter the exam note: '))
        result += exam

        validate(result, False)
    else:
        print(FAILED)

note_1 = float(input('Enter the first exam note: '))
note_2 = float(input('Enter the second exam note: '))
project = float(input('Enter project note: '))

result = ((note_1 * 4) + (note_2 * 4) + (project * 2)) / 10
validate(result, True)
