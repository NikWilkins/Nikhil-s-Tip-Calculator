Meal = float(input('Price of Meal:'))
TipPercent = float(input('Tip Percentage:'))
Tip = Meal * (TipPercent/100)
Total = Meal + Tip
print('Tip= ' + str(round(Tip,2)))
print('Total= ' + str(round(Total,2)))