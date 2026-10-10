with open("films.txt", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")
