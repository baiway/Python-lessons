with open("films.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        film = input(f"Favourite film #{i + 1}: ")
        file.write(film + "\n")

print("Saved your films to films.txt")
