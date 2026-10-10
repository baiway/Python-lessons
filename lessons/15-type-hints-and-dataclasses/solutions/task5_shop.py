from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    quantity: int


def get_price(item: Item) -> float:
    return item.price


stock = [
    Item("Notebook", 2.50, 40),
    Item("Pen", 0.80, 120),
    Item("Calculator", 12.99, 0),
    Item("Ruler", 1.20, 35),
    Item("Protractor", 1.50, 0),
]

total_value = sum([item.price * item.quantity for item in stock])
print(f"Total stock value: £{total_value:.2f}")

print("Cheapest to most expensive:")
for item in sorted(stock, key=get_price):
    print(f"  {item.name:<12} £{item.price:>6.2f}")

out_of_stock = [item.name for item in stock if item.quantity == 0]
print(f"Out of stock: {', '.join(out_of_stock)}")
