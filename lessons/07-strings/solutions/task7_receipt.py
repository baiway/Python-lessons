items = ["Bread", "Milk", "Cheddar cheese", "Apples"]
quantities = [1, 2, 1, 6]
prices = [1.35, 0.95, 3.50, 0.30]  # price of a single item, in £

# Header
print("=" * 42)
print(f"{'Item':<20}{'Qty':^7}{'Price':>15}")
print("-" * 42)

# One line per item
total = 0
for i in range(len(items)):
    line_price = quantities[i] * prices[i]
    total = total + line_price

    # Format the price first, so that the £ sign is included when aligning it
    price_text = f"£{line_price:.2f}"
    print(f"{items[i]:<20}{quantities[i]:^7}{price_text:>15}")

# Total
print("-" * 42)
total_text = f"£{total:.2f}"
print(f"{'Total':<27}{total_text:>15}")
print("=" * 42)
