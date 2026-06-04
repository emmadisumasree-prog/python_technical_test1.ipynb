# Coffee Shop Order System

orders = [
    'mocha', 'tea', 'Green tea', 'cold coffee',
    'Latte', 'Cappuccino', 'Espresso'
]

sizes = ['small-240', 'medium-320', 'large-360']

prices = {
    'mocha': 150,
    'tea': 100,
    'Green tea': 120,
    'cold coffee': 130,
    'Latte': 140,
    'Cappuccino': 160,
    'Espresso': 170
}

addons = ['biscuit', 'cookies']

print("Welcome to Coffee Shop")

print("Available Orders:")
for item in orders:
    print(item)

order = input("Enter your order: ")

if order in prices:
    size = input("Enter size (small-240 / medium-320 / large-360): ")
    quantity = int(input("Enter quantity: "))

    total_price = prices[order] * quantity

    add_on = input("Enter add-on (biscuit/cookies/none): ")

    if add_on in addons:
        addon_price = 20 * quantity
        total_price += addon_price
    else:
        addon_price = 0

    discount = 0

    if total_price > 700:
        discount = total_price * 0.15
        total_price = total_price - discount

    print("\n----- BILL -----")
    print("Order:", order)
    print("Size:", size)
    print("Quantity:", quantity)
    print("Add-on:", add_on)
    print("Discount:", discount)
    print("Total Price:", total_price)

else:
    print("Invalid order")