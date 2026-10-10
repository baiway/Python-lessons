first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
full_name = first_name + " " + surname

print(f"Initials: {first_name[0]}.{surname[0]}.")
print(f"Reversed: {full_name[::-1]}")
print(f"Number of letters: {len(first_name) + len(surname)}")
print(f"First three letters of surname: {surname[:3]}")
