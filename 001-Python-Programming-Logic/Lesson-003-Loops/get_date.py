from datetime import datetime as date

now = date.now()

print(f'Now - {now}')
print(f'dd/mm/YY - {now.strftime("%d/%m/%Y")}')
print(f'Textual month, day and year - {now.strftime("%B %d, %Y")}')
print(f'mm/dd/y - {now.strftime("%m/%d/%y")}')
print(f'Month abbreviation, day and year - {now.strftime("%b-%d-%Y")}')
print(f'dd/mm/YY H:M:S - {now.strftime("%d/%m/%Y %H:%M:%S")}')
