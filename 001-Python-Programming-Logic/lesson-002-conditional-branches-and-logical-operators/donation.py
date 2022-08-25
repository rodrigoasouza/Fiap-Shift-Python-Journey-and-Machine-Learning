print("DONATIONS MANAGEMENT")
donation = float(input("Please enter the donation amount received: R$"));

if(donation < 1000.00):
    percentage = 0.05
else:
    percentage = 0.15

investment = donation * percentage
immediate_use = donation - investment

print(f'The donation of R${donation} implies an investment of R${investment}, leaving R${immediate_use} for immediate use')