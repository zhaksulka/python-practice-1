# Task A1 — Multi-Item Shopping

name = input("Enter customer name: ")

subtotal = 0
item_count = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    
    if product.lower() == "done":
        break
    
    price = float(input("Enter price: "))
    
    subtotal += price
    item_count += 1

print("Customer :", name.upper())
print("Items :", item_count)
print("Subtotal :", subtotal, "KZT")


# Task A2 — Tiered Discount

if subtotal < 3000:
    discount_rate = 0
    tier = "No discount"
elif subtotal < 7000:
    discount_rate = 0.05
    tier = "5% discount"
else:
    discount_rate = 0.15
    tier = "15% discount"

discount_amount = subtotal * discount_rate
total = subtotal - discount_amount

print("------------------------------")
print("Discount tier :", tier)
print("Discount :", discount_amount, "KZT")
print("Total :", total, "KZT")


# Task A3 — Name Analysis

print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if len(name) > 5:
    print("Long name")
else:
    print("Short name")