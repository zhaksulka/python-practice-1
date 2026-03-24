# Input
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

# Calculations
subtotal = price * quantity
discount = subtotal * 0.10 if subtotal > 5000 else 0
total = subtotal - discount

# Output
print("=" * 30)
print("         SHOP RECEIPT")
print("=" * 30)
print("Customer :", customer_name)
print("Product :", product_name)
print("Price :", price, "KZT")
print("Quantity :", quantity)
print("-" * 30)
print("Subtotal :", subtotal, "KZT")
print("Discount :", discount, "KZT")
print("Total :", total, "KZT")
print("=" * 30)

# Comparison
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)