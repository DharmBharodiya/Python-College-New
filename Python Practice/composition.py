# composition - it is the stronger version of aggregation in python
# here the parent class, or the container class is responsible for the lifecycle of the other part classes
# those part classes cannot exist without the main container class
# it has a 'part-of' relationship or  'contained-by'

class Room:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Room: {self.name}"

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []  # Composition: House "contains" Room objects

    def add_room(self, room_name):
        room = Room(room_name) # here the room is created inside the house, so it cannot exist if the house don't exist somehow
        self.rooms.append(room)

    def list_rooms(self):
        for room in self.rooms:
            print(room)

house = House("SilverStone Villa Road")
house.add_room("Dharm's Room")
house.add_room("Tia's Rooms")

house.list_rooms()
