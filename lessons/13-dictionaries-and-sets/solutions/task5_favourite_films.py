ada_films = ["Spirited Away", "Paddington 2", "The Matrix", "Up", "Arrival"]
alan_films = ["The Matrix", "Inception", "Up", "Hidden Figures", "Arrival"]

ada = set(ada_films)
alan = set(alan_films)

# Sets have no order, so I've sorted them to make the output easier to read
print(f"Both like: {sorted(ada & alan)}")
print(f"At least one likes: {sorted(ada | alan)}")
print(f"Only Ada likes: {sorted(ada - alan)}")
print(f"Only one of them likes: {sorted(ada ^ alan)}")
