actual_cost = float(input('please enter the actual product price: '))
sale_price = float(input('please enter the selling price of the product 10'))
if sale_price>actual_cost:
    profit = sale_price-actual_cost
    print(f'total profit = {profit}')
else:
    print('no profit')
