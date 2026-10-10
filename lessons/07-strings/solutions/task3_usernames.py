def make_username(first_name, surname, year):
    """Returns a username made from the first three letters of `surname`, the
    first letter of `first_name` and the last two digits of `year`"""
    first_name = first_name.strip().lower()
    surname = surname.strip().lower()
    return surname[:3] + first_name[0] + str(year)[-2:]


print(make_username("Ada", "Lovelace", 2026))          # lova26
print(make_username("  ALAN ", " Turing  ", 2025))     # tura25
print(make_username("Grace", "Hopper", 2027))          # hopg27
