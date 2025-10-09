item_price = int(input('item price? '))
sales_amount = int(input('sales amount in %?'))

price_with_discount = item_price * (100 - sales_amount)/100

print(f"item price with all discounts = {price_with_discount}")