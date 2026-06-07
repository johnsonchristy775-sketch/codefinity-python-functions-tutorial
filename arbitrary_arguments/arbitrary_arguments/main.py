def calculate_total(*prices):
    if len(prices) == 0:
        return "Your cart is empty."

    total = sum(prices)

    if total >= 200:
        total *= .80  # 20% discount
    elif 200 > total >= 100:
        total *= .90  # 10% discount
    else:
        pass

    return f"Final total: ${total:.2f}"

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())