def calculate_total(price, quantity):
    """Returns total amount for given price and quantity"""
    total = price * quantity
    return total

bill_amount = calculate_total(250, 3)
print(f"Total Bill: ₹{bill_amount}")

