##Project 4: Mini Market Basket
print("Welcome to the Mini Market!")

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
basket = []
total_price = 0

while len(basket) < 3:
    product = input("Enter a product: ")
    if product in products:
        basket.append(product)
        total_price += products[product]
    else:
        print("warning - Product not found.")

print(f"Your basket: {', '.join(basket)}")
print(f"Total price: {total_price} TL")