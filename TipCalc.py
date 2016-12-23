def mealPrice():
    try:
        meal = float(input('Price of Meal:'))
        return meal
    except NameError:
        print('Please use integers')
        mealPrice()

def tipPrice():
    try:
        tipPercent = float(input('Tip Percentage:'))
        return tipPercent
    except NameError:
        print('Please use integers')
        tipPrice()

Meal = mealPrice()
TipPercent = tipPrice()

Tip = Meal * (TipPercent/100)
Total = Meal + Tip
print('Tip= ' + str(round(Tip,2)))
print('Total= ' + str(round(Total,2)))