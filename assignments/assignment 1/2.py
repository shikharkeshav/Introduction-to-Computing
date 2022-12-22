grossIncome = int(input('Your Gross Income '))
dependents = int(input('No. of Dependents '))
taxableIncome = round(grossIncome) - 10000 -dependents*3000
a =taxableIncome *0.2
print('tax is: ',a)
