def get_material(material):
    return float(input(f'Enter the {material} weight: '))

gold = get_material('Gold')
silver = get_material('Silver')
bronze = get_material('Bronze')
weights = []

if gold >= silver and gold >= bronze:
    weights.append('GOLD')

    if gold == silver:
        weights.append('SILVER')

    if gold == bronze:
        weights.append('BRONZE')
elif silver >= bronze:
    weights.append('SILVER')

    if silver == bronze:
        weights.append('BRONZE')
else:
    weights.append('BRONZE')

print('List of heaviest materials entered')
for i in range(len(weights)):
    print(weights[i])
