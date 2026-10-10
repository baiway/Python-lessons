class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, address, room_sizes):
        self.address = address
        # Composition: the house creates its own rooms, and they belong to it
        self.rooms = []
        for name, area in room_sizes:
            self.rooms.append(Room(name, area))

    def total_area(self):
        return sum([room.area for room in self.rooms])


class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        # Aggregation: the players were created elsewhere and are passed in
        self.players.append(player)


house = House("1 Python Lane", [("Kitchen", 12), ("Lounge", 20), ("Bedroom", 15)])
print(house.total_area())  # prints 47

ada = Player("Ada")
alan = Player("Alan")
club = Team("Bletchley Rovers")
country = Team("England")
for team in [club, country]:
    team.add_player(ada)   # the same Player object can belong to both teams
club.add_player(alan)

for team in [club, country]:
    print(f"{team.name}: {[player.name for player in team.players]}")

# If the club is disbanded, its players still exist
del club
print(ada.name, alan.name)
