colours = ["red", "blue", "red", "green", "blue", "blue", "yellow", "red"]

# Only add each colour if we haven't seen it before
unique_colours = []
for colour in colours:
    if colour not in unique_colours:
        unique_colours.append(colour)

print(unique_colours)
