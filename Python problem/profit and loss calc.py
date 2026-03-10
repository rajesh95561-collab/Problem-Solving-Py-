# Write a program that takes user input for cost price and selling price, and determines whether it's a loss or a profit.

cost = int(input("enter the cost of the product"))
selling_price = int(input("enter the selling price"))

if cost < selling_price:
    amount = selling_price - cost
    print(f"it is a profitable selling , profit is {amount}")
else:
    amount = cost - selling_price
    print(f"it is a loss selling , loss is {amount}")