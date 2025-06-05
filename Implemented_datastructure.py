#step 1

inventory = {
    "apple": (10,2.6),
    "Banana": (20,1.6)
}
    
#step 2

inventory["Orange"] = (15,3.0)

del inventory["apple"]

inventory["Banana"] = (25,1.8)

#step 3

for item, (quantity, price) in inventory.items():
    print(f"{item}: Quantity = {quantity}, Price = ${price:.2f}")

def total_value(inventory):
    total = 0
    for quantity, price in inventory.values():
        total += quantity * price
    return total

print(f"Total inventory value: ${total_value(inventory):.2f}")